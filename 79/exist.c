bool isExist(char** board, char* word, int i, int j, int pos, int m, int n){
    if(word[pos] == '\0') return true;

    if(i < 0 || i >= m || j < 0 || j >= n) return false;
    if(board[i][j] != word[pos]) return false;
    board[i][j] = '*';
    bool res = isExist(board,word,i+1,j,pos+1,m,n) ||
               isExist(board,word,i-1,j,pos+1,m,n) ||
               isExist(board,word,i,j+1,pos+1,m,n) ||
               isExist(board,word,i,j-1,pos+1,m,n);
    board[i][j] = word[pos];
    return res;
}
bool exist(char** board, int boardRowSize, int boardColSize, char* word) {
    if(!boardRowSize || !boardColSize) return false;
    if(*word == '\0') return false;

    for(int i = 0;i < boardRowSize;i++){
        for(int j = 0;j < boardColSize;j++){
            if(isExist(board,word,i,j,0,boardRowSize,boardColSize)) return true;
        }
    }
    return false;
}
