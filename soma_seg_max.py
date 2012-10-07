#

from bloco import *

def generateSegmets(_list):
    """
    Recebe lista e procura valores positivos e negativos consecutivos,\n
    entao esses valores sao marcados como 'blocos' ou 'separadores' respectivamente.\n
    Entao e retornado uma lista segmentada.
    """

    segList = []
    index = 0
    start = 0
    end   = 0

    for x in _list:
        # Se for o ultimo da lista
        if index + 1 == len(_list):
            if _list[index] > 0:
                end  = index
                segList.append(Block(start, end, None, _list))
            else:
                pass

        elif x >= 0:
            index += 1
            if _list[index] < 0:
                end  = index - 1
                segList.append(Block(start, end, None, _list))
        elif x < 0:
             index += 1
             if _list[index] > 0:
                start = index

    return segList

def mergeSegments(index, segList, _list):
    """Recebe lista de segmentos e mescla dois indices consecutivos"""
    neighbor = index+1
    start = segList[index].start
    end = segList[neighbor].end
    mergedVal = Block(start, end, valList=_list)
    segList[index] = mergedVal
    segList.pop(neighbor)


def generateSegMaxBlocks(segList, _list, start=0):
    """Gera lista com os blocos de segmentos maiores possiveis"""

    index = start

    for x in segList[start:]:
        if len(segList) > index+1:
            block = Block(x.start, segList[index+1].end, val=None, valList=_list)
        else:
            return

        if block.value >= x.value and block.value >= segList[index+1].value:
            mergeSegments(index, segList, _list)
        else:
            # Entra na recursao, passando a lista segmentada a frente deste bloco
            generateSegMaxBlocks(segList, _list, start=block.end+1)

        index += 1

def maxSequence(lista):

    """Procura entre os blocos maximos gerados, qual e o maior, retornado seu valor"""

    finalSegs = generateSegmets(lista)

    tam = len(finalSegs)
    flag = False
    while not flag:
        generateSegMaxBlocks(finalSegs, lista)

        if tam == len(finalSegs):
           flag = True
        else:
            tam = len(finalSegs)

    maxVal = 0
    for index, i in enumerate(finalSegs):
        if finalSegs[maxVal].value < i.value:
            maxVal = index

    return finalSegs[maxVal]