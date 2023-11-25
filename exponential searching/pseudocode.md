__this is the furnished pseudocode for the exponential searching algorithm__

```bash
function ExponentialSearch(Array, Target)
    if Array is empty
        return -1
    end if

    if Array[0] == Target
        return 0
    end if

    # Find range for binary search by repeated doubling
    Index ← 1
    while Index < length(Array) and Array[Index] <= Target
        Index ← Index * 2
    end while

    # Call binary search for the found range
    return BinarySearch(Array, Index / 2, min(Index, length(Array) - 1), Target)
end function

function BinarySearch(Array, Left, Right, Target)
    while Left <= Right
        Mid ← Left + (Right - Left) / 2
        if Array[Mid] == Target
            return Mid
        else if Array[Mid] < Target
            Left ← Mid + 1
        else
            Right ← Mid - 1
        end if
    end while
    return -1
end function
```