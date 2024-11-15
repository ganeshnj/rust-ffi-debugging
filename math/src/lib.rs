#[no_mangle]
pub extern "C" fn rs_add(left: i32, right: i32) -> i32 {
    add(left, right)
}

pub fn add(left: i32, right: i32) -> i32 {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}