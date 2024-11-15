from ctypes import cdll
lib = cdll.LoadLibrary("/Users/ganesh.jangir/dd/rust-ffi-debugging/math/target/debug/libmath.dylib")

def add(a, b):
    return lib.rs_add(a, b)

# #[no_mangle]
# pub extern "C" fn rs_add(left: i32, right: i32) -> i32 {
#     add(left, right)
# }