import unittest

import cupy


class TestBasic(unittest.TestCase):
    # Covers CUDA Runtime and NVRTC.

    def test_ufunc(self):
        self.assertEqual(16, int(cupy.ones(16).sum()))

    def test_kernel(self):
        x1 = cupy.ones(16)
        x2 = cupy.ones(16)
        y = cupy.ElementwiseKernel(
            'T x1, T x2', 'T y', 'y = x1 + x2;', 'test_elementwise_add',
        )(x1, x2)
        self.assertTrue(bool(cupy.all(y == x1 + x2)))


class TestCuBlas(unittest.TestCase):
    def test_matmul(self):
        a = cupy.arange(16, dtype=cupy.float32).reshape(4, 4)
        cupy.matmul(a, a)


class TestCuFFT(unittest.TestCase):
    def test_fft(self):
        x = cupy.arange(100, dtype=cupy.float32).reshape(10, 10)
        cupy.fft.fft(x)


class TestCuRand(unittest.TestCase):
    def test_randn(self):
        rs = cupy.random.get_random_state()
        rs.randn(10)


class TestCuSparse(unittest.TestCase):
    def test_csr(self):
        m = cupy.array([[0, 1, 0, 2],
                        [0, 0, 0, 0],
                        [0, 0, 3, 0]], dtype=cupy.float32)
        cupy.sparse.csr_matrix(m)
