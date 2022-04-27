

class DataParser:

    def parseData(self, data):
        splittedRows = data.split('\n')
        splittedRows = splittedRows[6:]
        print(splittedRows)
        data = [
            {'jan': {}},
            {'feb': {}},
            {'mar': {}},
            {'apr': {}},
            {'may': {}},
            {'jun': {}},
            {'july': {}},
            {'aug': {}},
            {'spt': {}},
            {'oct': {}},
            {'nov': {}},
            {'dec': {}},
            {'win': {}},
            {'spr': {}},
            {'sum': {}},
            {'aut': {}},
            {'ann': {}},
        ]
        for col in splittedRows:
            cols = col.split('   ')
            print("cols",cols)
            index = 0
            for i in range(len(cols)):
                if (cols[i] != '' and index<18):

                    cols_values = cols[i].split('  ')
                    dataCell = data[index]
                    key = list(dataCell.keys())[0]
                    print(key)
                    dataCell[key][cols_values[1]] = cols_values[0]
                    print("cols_values",cols_values)
                    print("cols_values",cols_values[0],"cols_values",cols_values[1])
                    index += 1
        return data
