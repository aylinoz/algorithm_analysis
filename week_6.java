class AList implements List {
  private Object listArray[];
  private static final int defaultSize = 10;
  private int maxSize;
  private int listSize;
  private int curr;

  // Constructors
  // Create a new list object with maximum size "size"
  AList(int size) { 
    maxSize = size;
    listSize = curr = 0;
    listArray = new Object[size];
  }
  // Create a list with the default capacity
  AList() { this(defaultSize); }

  public void clear()
    { listSize = curr = 0; }

  // Insert "it" at current position
  public boolean insert(Object it) {
    if (listSize >= maxSize) return false;
    for (int i=listSize; i>curr; i--)
      listArray[i] = listArray[i-1];
    listArray[curr] = it;
    listSize++;
    return true;
  }

  // Append "it" to list
  public boolean append(Object it) {
    if (listSize >= maxSize) return false;
    listArray[listSize++] = it;
    return true;
  }

  // Remove and return the current element
  public Object remove() {
    if ((curr<0) || (curr>=listSize)) 
      return null;
    Object it = listArray[curr];
    for(int i=curr; i<listSize-1; i++) 
      listArray[i] = listArray[i+1];
    listSize--;
    return it;
  }

  public void moveToStart() { curr = 0; }
  public void moveToEnd() { curr = listSize; }
  public void prev() { if (curr != 0) curr--; }
  public void next() { if (curr < listSize) curr++; }
  public int length() { return listSize; }
  public int currPos() { return curr; }
  
  // Set current list position to "pos"
  public boolean moveToPos(int pos) {
    if ((pos < 0) || (pos > listSize)) return false;
    curr = pos;
    return true;
  }

  // Return true if current position is at end of the list
  public boolean isAtEnd() { return curr == listSize; }

  // Return the current element
  public Object getValue() {
    if ((curr < 0) || (curr >= listSize))
      return null;
    return listArray[curr];
  }
}