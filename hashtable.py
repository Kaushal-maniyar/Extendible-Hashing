def give_bin(num, l):
    str_num = str(bin(num)).replace('0b', '', 1)
    if len(str_num) >= l:
        print("Given binary : ", str_num)
        return str_num[len(str_num) - l:]
    else:
        diff = l - len(str_num)
        for i in range(diff):
            str_num = '0' + str_num
        print("Given binary : ", str_num)
        return str_num


class Hash:
    def __init__(self):
        self.global_depth = 1
        self.global_keys = []
        self.buckets = []
        self.hash_table = {}
        self.bucket_size = 3
        self.dis_hash_table = {}
        # making keys
        for i in range(2 ** self.global_depth):
            self.global_keys.append(give_bin(i, self.global_depth))
        # buckets
        for i in self.global_keys:
            self.buckets.append({i: []})
        self.make_hash_table()

    def add_bucket(self, bucket, local_key, numbers):
        local_len = len(local_key)
        self.buckets.remove(bucket)
        b1 = {f"0{local_key}": []}
        b2 = {f"1{local_key}": []}
        for num in numbers:
            num_bin = give_bin(num, local_len + 1)
            if num_bin == f"0{local_key}":
                b1[f"0{local_key}"].append(num)
            elif num_bin == f"1{local_key}":
                b2[f"1{local_key}"].append(num)
        # print(b1)
        self.buckets.append(b1)
        self.buckets.append(b2)
        if len(b1[f"0{local_key}"]) > self.bucket_size:
            self.split(b1, f"0{local_key}")
        elif len(b2[f"1{local_key}"]) > self.bucket_size:
            self.split(b2, f"1{local_key}")

    def make_hash_table(self):
        hash_table = {}
        for i in sorted(self.global_keys):
            for j in self.buckets:
                for k in j.keys():
                    if len(i) == len(k) and k == i:
                        hash_table[i] = j
                    else:
                        diff = len(i) - len(k)
                        new_key = i[diff:]
                        if k == new_key:
                            hash_table[i] = j
        self.hash_table = hash_table.copy()
        self.dis_hash_table = {}
        for key, bucket in self.hash_table.items():
            self.dis_hash_table[key] = bucket.copy()
        # self.dis_hash_table = self.hash_table.copy()
        for bucket in self.dis_hash_table.values():
            # print(bucket)
            print("bucket :", bucket)
            if type(bucket) is not int:
                for key in bucket.keys():
                    # print(key)
                    bucket['local_depth'] = len(str(key))
                    break
        self.dis_hash_table['global_depth'] = self.global_depth

    def insert(self, number):
        local_key = ''
        print("Global depth : ", self.global_depth)
        num_key = give_bin(number, self.global_depth)
        for i in self.hash_table[num_key].keys():
            local_key = i
        if len(self.hash_table[num_key][local_key]) < self.bucket_size:
            self.hash_table[num_key][local_key].append(number)
            # print(self.hash_table)
        else:
            self.hash_table[num_key][local_key].append(number)
            self.split(self.hash_table[num_key], local_key)

    def split(self, bucket, local_key):
        numbers = bucket[local_key]
        local_len = len(local_key)

        if self.global_depth < local_len + 1:
            self.global_keys = []
            self.global_depth = self.global_depth + 1
            for i in range(2 ** self.global_depth):
                self.global_keys.append(give_bin(i, self.global_depth))
        self.add_bucket(bucket, local_key, numbers)
        # print(self.global_keys)
        self.make_hash_table()

    def delete_number(self, number):
        bin_number = give_bin(number,self.global_depth)
        for i in self.hash_table[bin_number].values():
            if type(i) is list:
                i.remove(number)
