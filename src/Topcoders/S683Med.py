class Holder:
    need = 0
    sum = 0


class MoveStonesEasy:
    def get(self, x, y):
        a = list(x)
        b = list(y)
        if a == b:
            return 0
        if sum(a) != sum(b):
            return -1
        for i in range(0, len(a)):
            if a[i] < b[i]:
                return self.moves(a, b, i) + self.get(a,b)


    def moves(self, start, final, i):
        holder = Holder()
        holder.need = final[i] - start[i]
        holder.sum = 0
        for d in range(1, len(start)):
            self.takeFrom(start, final, i, i - d, holder, d)
            self.takeFrom(start, final, i, i + d, holder, d)
            if holder.need == 0: return holder.sum

        return holder.sum

    def takeFrom(self, start, final, takingIndex, index, holder, d):
        if index < 0 or index >= len(start):
            return
        if start[index] > final[index]:
            maxTake = start[index] - final[index]
            if maxTake >= holder.need:
                start[index] -= holder.need
                start[takingIndex] += holder.need
                holder.sum += holder.need * d
                holder.need = 0
            else:
                start[index] -= maxTake
                start[takingIndex] += maxTake
                holder.need -= maxTake
                holder.sum += maxTake * d


# print(MoveStonesEasy().get([3, 10, 0, 4, 0, 0, 0, 1, 0], [5, 5, 0, 7, 0, 0, 0, 0, 1]))
print(MoveStonesEasy().get([10,0],[0,10]))
