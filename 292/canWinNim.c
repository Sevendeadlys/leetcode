bool canWinNim(int n) {
    if(n < 1)
    {
        return false;
    }

    if((n%4) == 0)
    {
        return false;
    }
    else
    {
        return true;
    }
}
