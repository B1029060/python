chess_dict = {'1h': 'bking', '6c': 'wqueen'}    # Given dict

def isValidChessBoard(dict):    # Check the chessboard is valid or not
    chess_list = ['wpawn', 'bpawn', 'wknight', 'bknight', 'wbishop', 'bbishop', 'wrook', 'brook', 'wqueen', 'bqueen',
                  'wking', 'bking']
    right_cnt = 0
    for key, val in dict.items():
        pawn_cnt = 0
        val_cnt = 0
        for x in range(64):
            if key in f'{(x % 8) + 1}{chr(ord("a") + (x // 8))}':
                break
            elif x == 63:
                print('False')
                return 0
            if key in chess_list[0] or key in chess_list[1]:
                pawn_cnt += 1
        for y in chess_list:
            if val != y:
                val_cnt += 1
            if val_cnt == len(chess_list):
                print('False')
        if len(chess_dict) <= 16 and pawn_cnt <= 8:
            right_cnt += 1
        else:
            print('False')
        if right_cnt == len(chess_dict):
            print('True')

isValidChessBoard(chess_dict)
