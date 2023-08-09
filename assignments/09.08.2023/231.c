bool isPowerOfTwo(int n){
  if(n==0)
  {
    return false;
  }
  if(n%2==0 || n==1){
    if (n==0 || n==1)
    {
      return true;
    }
      return(isPowerOfTwo(n/2));
  }
  return false;
}