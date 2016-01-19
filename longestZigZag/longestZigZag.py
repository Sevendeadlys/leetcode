class ZigZag(object):
    def longestZigZag(self, sequence):
        seqlen = len(sequence)
        if seqlen < 2:
            return seqlen

        zz = {}
        length = 1
        for i in range(seqlen):
            zz[i] = (1,0)
            for j in range(i):
                bit = zz[j][1]
                condition = bit*(sequence[i] - sequence[j])
                if bit == 0 and sequence[j] != sequence[i]:
                    zz[i] = (zz[j][0]+1,sequence[i] - sequence[j])

                if condition < 0 and zz[i][0] <= (zz[j][0] + 1):
                    zz[i] = (zz[j][0] + 1,-bit)

                length = length if zz[i][0] < length else zz[i][0]
        return length
