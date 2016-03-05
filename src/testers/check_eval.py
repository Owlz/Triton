#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

from triton import *
from ast    import *

setArchitecture(ARCH.X86_64)

tests = [
    bvsub(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvsub(bv(0x12345678, 32), bv(0, 32)),
    bvsub(bv(0x12345678, 32), bv(1, 32)),
    bvsub(bv(0x12345678, 32), bv(2, 32)),
    bvsub(bv(0x12345678, 32), bv(3, 32)),
    bvsub(bv(0x12345678, 32), bv(32, 32)),
    bvsub(bv(0x12345678, 32), bv(64, 32)),
    bvsub(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvsub(bv(0xf2345678, 32), bv(0, 32)),
    bvsub(bv(0xf2345678, 32), bv(1, 32)),
    bvsub(bv(0xf2345678, 32), bv(2, 32)),
    bvsub(bv(0xf2345678, 32), bv(3, 32)),
    bvsub(bv(0xf2345678, 32), bv(32, 32)),
    bvsub(bv(0xf2345678, 32), bv(64, 32)),
    bvsub(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvadd(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvadd(bv(0x12345678, 32), bv(0, 32)),
    bvadd(bv(0x12345678, 32), bv(1, 32)),
    bvadd(bv(0x12345678, 32), bv(2, 32)),
    bvadd(bv(0x12345678, 32), bv(3, 32)),
    bvadd(bv(0x12345678, 32), bv(32, 32)),
    bvadd(bv(0x12345678, 32), bv(64, 32)),
    bvadd(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvadd(bv(0xf2345678, 32), bv(0, 32)),
    bvadd(bv(0xf2345678, 32), bv(1, 32)),
    bvadd(bv(0xf2345678, 32), bv(2, 32)),
    bvadd(bv(0xf2345678, 32), bv(3, 32)),
    bvadd(bv(0xf2345678, 32), bv(32, 32)),
    bvadd(bv(0xf2345678, 32), bv(64, 32)),
    bvadd(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvxor(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvxor(bv(0x12345678, 32), bv(0, 32)),
    bvxor(bv(0x12345678, 32), bv(1, 32)),
    bvxor(bv(0x12345678, 32), bv(2, 32)),
    bvxor(bv(0x12345678, 32), bv(3, 32)),
    bvxor(bv(0x12345678, 32), bv(32, 32)),
    bvxor(bv(0x12345678, 32), bv(64, 32)),
    bvxor(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvxor(bv(0xf2345678, 32), bv(0, 32)),
    bvxor(bv(0xf2345678, 32), bv(1, 32)),
    bvxor(bv(0xf2345678, 32), bv(2, 32)),
    bvxor(bv(0xf2345678, 32), bv(3, 32)),
    bvxor(bv(0xf2345678, 32), bv(32, 32)),
    bvxor(bv(0xf2345678, 32), bv(64, 32)),
    bvxor(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvor(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvor(bv(0x12345678, 32), bv(0, 32)),
    bvor(bv(0x12345678, 32), bv(1, 32)),
    bvor(bv(0x12345678, 32), bv(2, 32)),
    bvor(bv(0x12345678, 32), bv(3, 32)),
    bvor(bv(0x12345678, 32), bv(32, 32)),
    bvor(bv(0x12345678, 32), bv(64, 32)),
    bvor(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvor(bv(0xf2345678, 32), bv(0, 32)),
    bvor(bv(0xf2345678, 32), bv(1, 32)),
    bvor(bv(0xf2345678, 32), bv(2, 32)),
    bvor(bv(0xf2345678, 32), bv(3, 32)),
    bvor(bv(0xf2345678, 32), bv(32, 32)),
    bvor(bv(0xf2345678, 32), bv(64, 32)),
    bvor(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvand(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvand(bv(0x12345678, 32), bv(0, 32)),
    bvand(bv(0x12345678, 32), bv(1, 32)),
    bvand(bv(0x12345678, 32), bv(2, 32)),
    bvand(bv(0x12345678, 32), bv(3, 32)),
    bvand(bv(0x12345678, 32), bv(32, 32)),
    bvand(bv(0x12345678, 32), bv(64, 32)),
    bvand(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvand(bv(0xf2345678, 32), bv(0, 32)),
    bvand(bv(0xf2345678, 32), bv(1, 32)),
    bvand(bv(0xf2345678, 32), bv(2, 32)),
    bvand(bv(0xf2345678, 32), bv(3, 32)),
    bvand(bv(0xf2345678, 32), bv(32, 32)),
    bvand(bv(0xf2345678, 32), bv(64, 32)),
    bvand(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvnand(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvnand(bv(0x12345678, 32), bv(0, 32)),
    bvnand(bv(0x12345678, 32), bv(1, 32)),
    bvnand(bv(0x12345678, 32), bv(2, 32)),
    bvnand(bv(0x12345678, 32), bv(3, 32)),
    bvnand(bv(0x12345678, 32), bv(32, 32)),
    bvnand(bv(0x12345678, 32), bv(64, 32)),
    bvnand(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvnand(bv(0xf2345678, 32), bv(0, 32)),
    bvnand(bv(0xf2345678, 32), bv(1, 32)),
    bvnand(bv(0xf2345678, 32), bv(2, 32)),
    bvnand(bv(0xf2345678, 32), bv(3, 32)),
    bvnand(bv(0xf2345678, 32), bv(32, 32)),
    bvnand(bv(0xf2345678, 32), bv(64, 32)),
    bvnand(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvnor(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvnor(bv(0x12345678, 32), bv(0, 32)),
    bvnor(bv(0x12345678, 32), bv(1, 32)),
    bvnor(bv(0x12345678, 32), bv(2, 32)),
    bvnor(bv(0x12345678, 32), bv(3, 32)),
    bvnor(bv(0x12345678, 32), bv(32, 32)),
    bvnor(bv(0x12345678, 32), bv(64, 32)),
    bvnor(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvnor(bv(0xf2345678, 32), bv(0, 32)),
    bvnor(bv(0xf2345678, 32), bv(1, 32)),
    bvnor(bv(0xf2345678, 32), bv(2, 32)),
    bvnor(bv(0xf2345678, 32), bv(3, 32)),
    bvnor(bv(0xf2345678, 32), bv(32, 32)),
    bvnor(bv(0xf2345678, 32), bv(64, 32)),
    bvnor(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvxnor(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvxnor(bv(0x12345678, 32), bv(0, 32)),
    bvxnor(bv(0x12345678, 32), bv(1, 32)),
    bvxnor(bv(0x12345678, 32), bv(2, 32)),
    bvxnor(bv(0x12345678, 32), bv(3, 32)),
    bvxnor(bv(0x12345678, 32), bv(32, 32)),
    bvxnor(bv(0x12345678, 32), bv(64, 32)),
    bvxnor(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvxnor(bv(0xf2345678, 32), bv(0, 32)),
    bvxnor(bv(0xf2345678, 32), bv(1, 32)),
    bvxnor(bv(0xf2345678, 32), bv(2, 32)),
    bvxnor(bv(0xf2345678, 32), bv(3, 32)),
    bvxnor(bv(0xf2345678, 32), bv(32, 32)),
    bvxnor(bv(0xf2345678, 32), bv(64, 32)),
    bvxnor(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvmul(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvmul(bv(0x12345678, 32), bv(0, 32)),
    bvmul(bv(0x12345678, 32), bv(1, 32)),
    bvmul(bv(0x12345678, 32), bv(2, 32)),
    bvmul(bv(0x12345678, 32), bv(3, 32)),
    bvmul(bv(0x12345678, 32), bv(32, 32)),
    bvmul(bv(0x12345678, 32), bv(64, 32)),
    bvmul(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvmul(bv(0xf2345678, 32), bv(0, 32)),
    bvmul(bv(0xf2345678, 32), bv(1, 32)),
    bvmul(bv(0xf2345678, 32), bv(2, 32)),
    bvmul(bv(0xf2345678, 32), bv(3, 32)),
    bvmul(bv(0xf2345678, 32), bv(32, 32)),
    bvmul(bv(0xf2345678, 32), bv(64, 32)),
    bvmul(bv(0xf2345678, 32), bv(0x12345678, 32)),

    bvneg(bv(0x88888888, 32)),
    bvneg(bv(0x12345678, 32)),
    bvneg(bv(0x22345678, 32)),
    bvneg(bv(0x32345678, 32)),
    bvneg(bv(0x42345678, 32)),
    bvneg(bv(0x52345678, 32)),
    bvneg(bv(0x62345678, 32)),
    bvneg(bv(0x72345678, 32)),
    bvneg(bv(0x82345678, 32)),
    bvneg(bv(0x92345678, 32)),
    bvneg(bv(0xa2345678, 32)),
    bvneg(bv(0xb2345678, 32)),
    bvneg(bv(0xc2345678, 32)),
    bvneg(bv(0xd345678, 32)),
    bvneg(bv(0xe2345678, 32)),
    bvneg(bv(0xf2345678, 32)),
    bvneg(bv(0x1, 32)),
    bvneg(bv(0x2, 32)),
    bvneg(bv(0x3, 32)),
    bvneg(bv(0x4, 32)),
    bvneg(bv(0x5, 32)),
    bvneg(bv(0x6, 32)),
    bvneg(bv(0xa, 32)),
    bvneg(bv(0xe, 32)),
    bvneg(bv(0xf, 32)),
    bvneg(bv(0x1f, 32)),
    bvneg(bv(0x2f, 32)),
    bvneg(bv(0x3e, 32)),
    bvneg(bv(0xffff, 32)),

    bvnot(bv(0x88888888, 32)),
    bvnot(bv(0x12345678, 32)),
    bvnot(bv(0x22345678, 32)),
    bvnot(bv(0x32345678, 32)),
    bvnot(bv(0x42345678, 32)),
    bvnot(bv(0x52345678, 32)),
    bvnot(bv(0x62345678, 32)),
    bvnot(bv(0x72345678, 32)),
    bvnot(bv(0x82345678, 32)),
    bvnot(bv(0x92345678, 32)),
    bvnot(bv(0xa2345678, 32)),
    bvnot(bv(0xb2345678, 32)),
    bvnot(bv(0xc2345678, 32)),
    bvnot(bv(0xd345678, 32)),
    bvnot(bv(0xe2345678, 32)),
    bvnot(bv(0xf2345678, 32)),
    bvnot(bv(0x1, 32)),
    bvnot(bv(0x2, 32)),
    bvnot(bv(0x3, 32)),
    bvnot(bv(0x4, 32)),
    bvnot(bv(0x5, 32)),
    bvnot(bv(0x6, 32)),
    bvnot(bv(0xa, 32)),
    bvnot(bv(0xe, 32)),
    bvnot(bv(0xf, 32)),
    bvnot(bv(0x1f, 32)),
    bvnot(bv(0x2f, 32)),
    bvnot(bv(0x3e, 32)),
    bvnot(bv(0xffff, 32)),

    bvsdiv(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvsdiv(bv(0x12345678, 32), bv(0, 32)),
    bvsdiv(bv(0x12345678, 32), bv(1, 32)),
    bvsdiv(bv(0x12345678, 32), bv(2, 32)),
    bvsdiv(bv(0x12345678, 32), bv(3, 32)),
    bvsdiv(bv(0x12345678, 32), bv(32, 32)),
    bvsdiv(bv(0x12345678, 32), bv(64, 32)),
    bvsdiv(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvsdiv(bv(0xf2345678, 32), bv(0, 32)),
    bvsdiv(bv(0xf2345678, 32), bv(1, 32)),
    bvsdiv(bv(0xf2345678, 32), bv(2, 32)),
    bvsdiv(bv(0xf2345678, 32), bv(3, 32)),
    bvsdiv(bv(0xf2345678, 32), bv(32, 32)),
    bvsdiv(bv(0xf2345678, 32), bv(64, 32)),
    bvsdiv(bv(0xf2345678, 32), bv(0x12345678, 32)),
    bvsdiv(bv(0b10000000, 8), bv(0, 8)),
    bvsdiv(bv(0b10000000, 8), bv(1, 8)),
    bvsdiv(bv(0b10000000, 8), bv(2, 8)),
    bvsdiv(bv(0b10000000, 8), bv(3, 8)),
    bvsdiv(bv(0b10000000, 8), bv(4, 8)),
    bvsdiv(bv(0b10000000, 8), bv(5, 8)),
    bvsdiv(bv(0b10000000, 8), bv(6, 8)),
    bvsdiv(bv(0b10000000, 8), bv(7, 8)),
    bvsdiv(bv(0b10000000, 8), bv(8, 8)),
    bvsdiv(bv(0b10000000, 8), bv(9, 8)),
    bvsdiv(bv(0b10000000, 8), bv(123, 8)),
    bvsdiv(bv(0b10001000, 8), bv(0, 8)),
    bvsdiv(bv(0b10001000, 8), bv(1, 8)),
    bvsdiv(bv(0b10001000, 8), bv(2, 8)),
    bvsdiv(bv(0b10001000, 8), bv(3, 8)),
    bvsdiv(bv(0b10001000, 8), bv(4, 8)),
    bvsdiv(bv(0b10001000, 8), bv(5, 8)),
    bvsdiv(bv(0b10001000, 8), bv(6, 8)),
    bvsdiv(bv(0b10001000, 8), bv(7, 8)),
    bvsdiv(bv(0b10001000, 8), bv(8, 8)),
    bvsdiv(bv(0b10001000, 8), bv(9, 8)),
    bvsdiv(bv(0b10001000, 8), bv(123, 8)),
    bvsdiv(bv(0b00010001, 8), bv(0b00000001, 8)),
    bvsdiv(bv(0b00010010, 8), bv(0b00000010, 8)),
    bvsdiv(bv(0b00010100, 8), bv(0b00000100, 8)),
    bvsdiv(bv(0b00001000, 8), bv(0b00001000, 8)),
    bvsdiv(bv(0b00010000, 8), bv(0b00010000, 8)),
    bvsdiv(bv(0b00100000, 8), bv(0b00100000, 8)),
    bvsdiv(bv(0b01000000, 8), bv(0b01000001, 8)),
    bvsdiv(bv(0b10000000, 8), bv(0b10000010, 8)),
    bvsdiv(bv(0b01000000, 8), bv(0b00000011, 8)),
    bvsdiv(bv(0b00100000, 8), bv(0b00000101, 8)),
    bvsdiv(bv(0b00010000, 8), bv(0b00000110, 8)),
    bvsdiv(bv(0b0010001, 7), bv(0b0000001, 7)),
    bvsdiv(bv(0b0010010, 7), bv(0b0000010, 7)),
    bvsdiv(bv(0b0010100, 7), bv(0b0000100, 7)),
    bvsdiv(bv(0b0001000, 7), bv(0b0001000, 7)),
    bvsdiv(bv(0b0010000, 7), bv(0b0010000, 7)),
    bvsdiv(bv(0b0100000, 7), bv(0b0100000, 7)),
    bvsdiv(bv(0b0000000, 7), bv(0b0000001, 7)),
    bvsdiv(bv(0b1000000, 7), bv(0b1000010, 7)),
    bvsdiv(bv(0b0000000, 7), bv(0b0000100, 7)),
    bvsdiv(bv(0b0100000, 7), bv(0b0000110, 7)),
    bvsdiv(bv(0b0010000, 7), bv(0b0000111, 7)),

    bvudiv(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvudiv(bv(0x12345678, 32), bv(0, 32)),
    bvudiv(bv(0x12345678, 32), bv(1, 32)),
    bvudiv(bv(0x12345678, 32), bv(2, 32)),
    bvudiv(bv(0x12345678, 32), bv(3, 32)),
    bvudiv(bv(0x12345678, 32), bv(32, 32)),
    bvudiv(bv(0x12345678, 32), bv(64, 32)),
    bvudiv(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvudiv(bv(0xf2345678, 32), bv(0, 32)),
    bvudiv(bv(0xf2345678, 32), bv(1, 32)),
    bvudiv(bv(0xf2345678, 32), bv(2, 32)),
    bvudiv(bv(0xf2345678, 32), bv(3, 32)),
    bvudiv(bv(0xf2345678, 32), bv(32, 32)),
    bvudiv(bv(0xf2345678, 32), bv(64, 32)),
    bvudiv(bv(0xf2345678, 32), bv(0x12345678, 32)),
    bvudiv(bv(0b10000000, 8), bv(0, 8)),
    bvudiv(bv(0b10000000, 8), bv(1, 8)),
    bvudiv(bv(0b10000000, 8), bv(2, 8)),
    bvudiv(bv(0b10000000, 8), bv(3, 8)),
    bvudiv(bv(0b10000000, 8), bv(4, 8)),
    bvudiv(bv(0b10000000, 8), bv(5, 8)),
    bvudiv(bv(0b10000000, 8), bv(6, 8)),
    bvudiv(bv(0b10000000, 8), bv(7, 8)),
    bvudiv(bv(0b10000000, 8), bv(8, 8)),
    bvudiv(bv(0b10000000, 8), bv(9, 8)),
    bvudiv(bv(0b10000000, 8), bv(123, 8)),
    bvudiv(bv(0b10001000, 8), bv(0, 8)),
    bvudiv(bv(0b10001000, 8), bv(1, 8)),
    bvudiv(bv(0b10001000, 8), bv(2, 8)),
    bvudiv(bv(0b10001000, 8), bv(3, 8)),
    bvudiv(bv(0b10001000, 8), bv(4, 8)),
    bvudiv(bv(0b10001000, 8), bv(5, 8)),
    bvudiv(bv(0b10001000, 8), bv(6, 8)),
    bvudiv(bv(0b10001000, 8), bv(7, 8)),
    bvudiv(bv(0b10001000, 8), bv(8, 8)),
    bvudiv(bv(0b10001000, 8), bv(9, 8)),
    bvudiv(bv(0b10001000, 8), bv(123, 8)),
    bvudiv(bv(0b00010001, 8), bv(0b00000001, 8)),
    bvudiv(bv(0b00010010, 8), bv(0b00000010, 8)),
    bvudiv(bv(0b00010100, 8), bv(0b00000100, 8)),
    bvudiv(bv(0b00001000, 8), bv(0b00001000, 8)),
    bvudiv(bv(0b00010000, 8), bv(0b00010000, 8)),
    bvudiv(bv(0b00100000, 8), bv(0b00100000, 8)),
    bvudiv(bv(0b01000000, 8), bv(0b01000001, 8)),
    bvudiv(bv(0b10000000, 8), bv(0b10000010, 8)),
    bvudiv(bv(0b01000000, 8), bv(0b00000011, 8)),
    bvudiv(bv(0b00100000, 8), bv(0b00000101, 8)),
    bvudiv(bv(0b00010000, 8), bv(0b00000110, 8)),
    bvudiv(bv(0b0010001, 7), bv(0b0000001, 7)),
    bvudiv(bv(0b0010010, 7), bv(0b0000010, 7)),
    bvudiv(bv(0b0010100, 7), bv(0b0000100, 7)),
    bvudiv(bv(0b0001000, 7), bv(0b0001000, 7)),
    bvudiv(bv(0b0010000, 7), bv(0b0010000, 7)),
    bvudiv(bv(0b0100000, 7), bv(0b0100000, 7)),
    bvudiv(bv(0b0000000, 7), bv(0b0000001, 7)),
    bvudiv(bv(0b1000000, 7), bv(0b1000010, 7)),
    bvudiv(bv(0b0000000, 7), bv(0b0000100, 7)),
    bvudiv(bv(0b0100000, 7), bv(0b0000110, 7)),
    bvudiv(bv(0b0010000, 7), bv(0b0000111, 7)),

    bvashr(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvashr(bv(0x12345678, 32), bv(0, 32)),
    bvashr(bv(0x12345678, 32), bv(1, 32)),
    bvashr(bv(0x12345678, 32), bv(2, 32)),
    bvashr(bv(0x12345678, 32), bv(3, 32)),
    bvashr(bv(0x12345678, 32), bv(32, 32)),
    bvashr(bv(0x12345678, 32), bv(64, 32)),
    bvashr(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvashr(bv(0xf2345678, 32), bv(0, 32)),
    bvashr(bv(0xf2345678, 32), bv(1, 32)),
    bvashr(bv(0xf2345678, 32), bv(2, 32)),
    bvashr(bv(0xf2345678, 32), bv(3, 32)),
    bvashr(bv(0xf2345678, 32), bv(32, 32)),
    bvashr(bv(0xf2345678, 32), bv(64, 32)),
    bvashr(bv(0xf2345678, 32), bv(0x12345678, 32)),
    bvashr(bv(0b10000000, 8), bv(0, 8)),
    bvashr(bv(0b10000000, 8), bv(1, 8)),
    bvashr(bv(0b10000000, 8), bv(2, 8)),
    bvashr(bv(0b10000000, 8), bv(3, 8)),
    bvashr(bv(0b10000000, 8), bv(4, 8)),
    bvashr(bv(0b10000000, 8), bv(5, 8)),
    bvashr(bv(0b10000000, 8), bv(6, 8)),
    bvashr(bv(0b10000000, 8), bv(7, 8)),
    bvashr(bv(0b10000000, 8), bv(8, 8)),
    bvashr(bv(0b10000000, 8), bv(9, 8)),
    bvashr(bv(0b10000000, 8), bv(123, 8)),
    bvashr(bv(0b10001000, 8), bv(0, 8)),
    bvashr(bv(0b10001000, 8), bv(1, 8)),
    bvashr(bv(0b10001000, 8), bv(2, 8)),
    bvashr(bv(0b10001000, 8), bv(3, 8)),
    bvashr(bv(0b10001000, 8), bv(4, 8)),
    bvashr(bv(0b10001000, 8), bv(5, 8)),
    bvashr(bv(0b10001000, 8), bv(6, 8)),
    bvashr(bv(0b10001000, 8), bv(7, 8)),
    bvashr(bv(0b10001000, 8), bv(8, 8)),
    bvashr(bv(0b10001000, 8), bv(9, 8)),
    bvashr(bv(0b10001000, 8), bv(123, 8)),
    bvashr(bv(0b00010001, 8), bv(0b00000001, 8)),
    bvashr(bv(0b00010010, 8), bv(0b00000010, 8)),
    bvashr(bv(0b00010100, 8), bv(0b00000100, 8)),
    bvashr(bv(0b00001000, 8), bv(0b00001000, 8)),
    bvashr(bv(0b00010000, 8), bv(0b00010000, 8)),
    bvashr(bv(0b00100000, 8), bv(0b00100000, 8)),
    bvashr(bv(0b01000000, 8), bv(0b01000001, 8)),
    bvashr(bv(0b10000000, 8), bv(0b10000010, 8)),
    bvashr(bv(0b01000000, 8), bv(0b00000011, 8)),
    bvashr(bv(0b00100000, 8), bv(0b00000101, 8)),
    bvashr(bv(0b00010000, 8), bv(0b00000110, 8)),
    bvashr(bv(0b0010001, 7), bv(0b0000001, 7)),
    bvashr(bv(0b0010010, 7), bv(0b0000010, 7)),
    bvashr(bv(0b0010100, 7), bv(0b0000100, 7)),
    bvashr(bv(0b0001000, 7), bv(0b0001000, 7)),
    bvashr(bv(0b0010000, 7), bv(0b0010000, 7)),
    bvashr(bv(0b0100000, 7), bv(0b0100000, 7)),
    bvashr(bv(0b0000000, 7), bv(0b0000001, 7)),
    bvashr(bv(0b1000000, 7), bv(0b1000010, 7)),
    bvashr(bv(0b0000000, 7), bv(0b0000100, 7)),
    bvashr(bv(0b0100000, 7), bv(0b0000110, 7)),
    bvashr(bv(0b0010000, 7), bv(0b0000111, 7)),
    bvashr(bv(0xfe00000000000000, 64), bv(8, 64)),

    bvlshr(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvlshr(bv(0x12345678, 32), bv(0, 32)),
    bvlshr(bv(0x12345678, 32), bv(1, 32)),
    bvlshr(bv(0x12345678, 32), bv(2, 32)),
    bvlshr(bv(0x12345678, 32), bv(3, 32)),
    bvlshr(bv(0x12345678, 32), bv(32, 32)),
    bvlshr(bv(0x12345678, 32), bv(64, 32)),
    bvlshr(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvlshr(bv(0xf2345678, 32), bv(0, 32)),
    bvlshr(bv(0xf2345678, 32), bv(1, 32)),
    bvlshr(bv(0xf2345678, 32), bv(2, 32)),
    bvlshr(bv(0xf2345678, 32), bv(3, 32)),
    bvlshr(bv(0xf2345678, 32), bv(4, 32)),
    bvlshr(bv(0xf2345678, 32), bv(5, 32)),
    bvlshr(bv(0xf2345678, 32), bv(6, 32)),
    bvlshr(bv(0xf2345678, 32), bv(32, 32)),
    bvlshr(bv(0xf2345678, 32), bv(64, 32)),
    bvlshr(bv(0xf2345678, 32), bv(0x12345678, 32)),
    bvlshr(bv(0b10000000, 8), bv(0, 8)),
    bvlshr(bv(0b10000000, 8), bv(1, 8)),
    bvlshr(bv(0b10000000, 8), bv(2, 8)),
    bvlshr(bv(0b10000000, 8), bv(3, 8)),
    bvlshr(bv(0b10000000, 8), bv(4, 8)),
    bvlshr(bv(0b10000000, 8), bv(5, 8)),
    bvlshr(bv(0b10000000, 8), bv(6, 8)),
    bvlshr(bv(0b10000000, 8), bv(7, 8)),
    bvlshr(bv(0b10000000, 8), bv(8, 8)),
    bvlshr(bv(0b10000000, 8), bv(9, 8)),
    bvlshr(bv(0b10000000, 8), bv(123, 8)),
    bvlshr(bv(0b10001000, 8), bv(0, 8)),
    bvlshr(bv(0b10001000, 8), bv(1, 8)),
    bvlshr(bv(0b10001000, 8), bv(2, 8)),
    bvlshr(bv(0b10001000, 8), bv(3, 8)),
    bvlshr(bv(0b10001000, 8), bv(4, 8)),
    bvlshr(bv(0b10001000, 8), bv(5, 8)),
    bvlshr(bv(0b10001000, 8), bv(6, 8)),
    bvlshr(bv(0b10001000, 8), bv(7, 8)),
    bvlshr(bv(0b10001000, 8), bv(8, 8)),
    bvlshr(bv(0b10001000, 8), bv(9, 8)),
    bvlshr(bv(0b10001000, 8), bv(123, 8)),

    bvshl(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvshl(bv(0x12345678, 32), bv(0, 32)),
    bvshl(bv(0x12345678, 32), bv(1, 32)),
    bvshl(bv(0x12345678, 32), bv(2, 32)),
    bvshl(bv(0x12345678, 32), bv(3, 32)),
    bvshl(bv(0x12345678, 32), bv(32, 32)),
    bvshl(bv(0x12345678, 32), bv(64, 32)),
    bvshl(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvshl(bv(0xf2345678, 32), bv(0, 32)),
    bvshl(bv(0xf2345678, 32), bv(1, 32)),
    bvshl(bv(0xf2345678, 32), bv(2, 32)),
    bvshl(bv(0xf2345678, 32), bv(3, 32)),
    bvshl(bv(0xf2345678, 32), bv(32, 32)),
    bvshl(bv(0xf2345678, 32), bv(64, 32)),
    bvshl(bv(0xf2345678, 32), bv(0x12345678, 32)),
    bvshl(bv(0b00000001, 8), bv(0, 8)),
    bvshl(bv(0b00000001, 8), bv(1, 8)),
    bvshl(bv(0b00000001, 8), bv(2, 8)),
    bvshl(bv(0b00000001, 8), bv(3, 8)),
    bvshl(bv(0b00000001, 8), bv(4, 8)),
    bvshl(bv(0b00000001, 8), bv(5, 8)),
    bvshl(bv(0b00000001, 8), bv(6, 8)),
    bvshl(bv(0b00000001, 8), bv(7, 8)),
    bvshl(bv(0b00000001, 8), bv(8, 8)),
    bvshl(bv(0b00000001, 8), bv(9, 8)),
    bvshl(bv(0b00000001, 8), bv(123, 8)),
    bvshl(bv(0b00000001, 8), bv(0, 8)),
    bvshl(bv(0b00000011, 8), bv(1, 8)),
    bvshl(bv(0b00000101, 8), bv(2, 8)),
    bvshl(bv(0b00001001, 8), bv(3, 8)),
    bvshl(bv(0b00010001, 8), bv(4, 8)),
    bvshl(bv(0b00100001, 8), bv(5, 8)),
    bvshl(bv(0b01000001, 8), bv(6, 8)),
    bvshl(bv(0b10000011, 8), bv(7, 8)),
    bvshl(bv(0b01000101, 8), bv(8, 8)),
    bvshl(bv(0b00101001, 8), bv(9, 8)),
    bvshl(bv(0b00010001, 8), bv(123, 8)),

    bvrol(0x88888888, bv(0x99999999, 32)),
    bvrol(0x12345678, bv(0, 32)),
    bvrol(0x12345678, bv(1, 32)),
    bvrol(0x12345678, bv(2, 32)),
    bvrol(0x12345678, bv(3, 32)),
    bvrol(0x12345678, bv(32, 32)),
    bvrol(0x12345678, bv(64, 32)),
    bvrol(0x12345678, bv(0x12345678, 32)),
    bvrol(0xf2345678, bv(0, 32)),
    bvrol(0xf2345678, bv(1, 32)),
    bvrol(0xf2345678, bv(2, 32)),
    bvrol(0xf2345678, bv(3, 32)),
    bvrol(0xf2345678, bv(32, 32)),
    bvrol(0xf2345678, bv(64, 32)),
    bvrol(0xf2345678, bv(0x12345678, 32)),

    bvrol(0x99999999, bv(0x88888888, 32)),
    bvrol(0, bv(0x12345678, 32)),
    bvrol(1, bv(0x12345678, 32)),
    bvrol(2, bv(0x12345678, 32)),
    bvrol(3, bv(0x12345678, 32)),
    bvrol(32, bv(0x12345678, 32)),
    bvrol(64, bv(0x12345678, 32)),
    bvrol(0x12345678, bv(0x12345678, 32)),
    bvrol(0, bv(0xf2345678, 32)),
    bvrol(1, bv(0xf2345678, 32)),
    bvrol(2, bv(0xf2345678, 32)),
    bvrol(3, bv(0xf2345678, 32)),
    bvrol(32, bv(0xf2345678, 32)),
    bvrol(64, bv(0xf2345678, 32)),
    bvrol(0x12345678, bv(0xf2345678, 32)),

    bvror(0x88888888, bv(0x99999999, 32)),
    bvror(0x12345678, bv(0, 32)),
    bvror(0x12345678, bv(1, 32)),
    bvror(0x12345678, bv(2, 32)),
    bvror(0x12345678, bv(3, 32)),
    bvror(0x12345678, bv(32, 32)),
    bvror(0x12345678, bv(64, 32)),
    bvror(0x12345678, bv(0x12345678, 32)),
    bvror(0xf2345678, bv(0, 32)),
    bvror(0xf2345678, bv(1, 32)),
    bvror(0xf2345678, bv(2, 32)),
    bvror(0xf2345678, bv(3, 32)),
    bvror(0xf2345678, bv(32, 32)),
    bvror(0xf2345678, bv(64, 32)),
    bvror(0xf2345678, bv(0x12345678, 32)),

    bvror(0x99999999, bv(0x88888888, 32)),
    bvror(0, bv(0x12345678, 32)),
    bvror(1, bv(0x12345678, 32)),
    bvror(2, bv(0x12345678, 32)),
    bvror(3, bv(0x12345678, 32)),
    bvror(32, bv(0x12345678, 32)),
    bvror(64, bv(0x12345678, 32)),
    bvror(0x12345678, bv(0x12345678, 32)),
    bvror(0, bv(0xf2345678, 32)),
    bvror(1, bv(0xf2345678, 32)),
    bvror(2, bv(0xf2345678, 32)),
    bvror(3, bv(0xf2345678, 32)),
    bvror(32, bv(0xf2345678, 32)),
    bvror(64, bv(0xf2345678, 32)),
    bvror(0x12345678, bv(0xf2345678, 32)),

    bvsmod(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvsmod(bv(0x12345678, 32), bv(0, 32)),
    bvsmod(bv(0x12345678, 32), bv(1, 32)),
    bvsmod(bv(0x12345678, 32), bv(2, 32)),
    bvsmod(bv(0x12345678, 32), bv(3, 32)),
    bvsmod(bv(0x12345678, 32), bv(32, 32)),
    bvsmod(bv(0x12345678, 32), bv(64, 32)),
    bvsmod(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvsmod(bv(0xf2345678, 32), bv(0, 32)),
    bvsmod(bv(0xf2345678, 32), bv(1, 32)),
    bvsmod(bv(0xf2345678, 32), bv(2, 32)),
    bvsmod(bv(0xf2345678, 32), bv(3, 32)),
    bvsmod(bv(0xf2345678, 32), bv(32, 32)),
    bvsmod(bv(0xf2345678, 32), bv(64, 32)),
    bvsmod(bv(0xf2345678, 32), bv(0x12345678, 32)),
    bvsmod(bv(0b10000000, 8), bv(0, 8)),
    bvsmod(bv(0b10000000, 8), bv(1, 8)),
    bvsmod(bv(0b10000000, 8), bv(2, 8)),
    bvsmod(bv(0b10000000, 8), bv(3, 8)),
    bvsmod(bv(0b10000000, 8), bv(4, 8)),
    bvsmod(bv(0b10000000, 8), bv(5, 8)),
    bvsmod(bv(0b10000000, 8), bv(6, 8)),
    bvsmod(bv(0b10000000, 8), bv(7, 8)),
    bvsmod(bv(0b10000000, 8), bv(8, 8)),
    bvsmod(bv(0b10000000, 8), bv(9, 8)),
    bvsmod(bv(0b10000000, 8), bv(123, 8)),
    bvsmod(bv(0b10001000, 8), bv(0, 8)),
    bvsmod(bv(0b10001000, 8), bv(1, 8)),
    bvsmod(bv(0b10001000, 8), bv(2, 8)),
    bvsmod(bv(0b10001000, 8), bv(3, 8)),
    bvsmod(bv(0b10001000, 8), bv(4, 8)),
    bvsmod(bv(0b10001000, 8), bv(5, 8)),
    bvsmod(bv(0b10001000, 8), bv(6, 8)),
    bvsmod(bv(0b10001000, 8), bv(7, 8)),
    bvsmod(bv(0b10001000, 8), bv(8, 8)),
    bvsmod(bv(0b10001000, 8), bv(9, 8)),
    bvsmod(bv(0b10001000, 8), bv(123, 8)),
    bvsmod(bv(0b00010001, 8), bv(0b00000001, 8)),
    bvsmod(bv(0b00010010, 8), bv(0b00000010, 8)),
    bvsmod(bv(0b00010100, 8), bv(0b00000100, 8)),
    bvsmod(bv(0b00001000, 8), bv(0b00001000, 8)),
    bvsmod(bv(0b00010000, 8), bv(0b00010000, 8)),
    bvsmod(bv(0b00100000, 8), bv(0b00100000, 8)),
    bvsmod(bv(0b01000000, 8), bv(0b01000001, 8)),
    bvsmod(bv(0b10000000, 8), bv(0b10000010, 8)),
    bvsmod(bv(0b01000000, 8), bv(0b00000011, 8)),
    bvsmod(bv(0b00100000, 8), bv(0b00000101, 8)),
    bvsmod(bv(0b00010000, 8), bv(0b00000110, 8)),
    bvsmod(bv(0b0010001, 7), bv(0b0000001, 7)),
    bvsmod(bv(0b0010010, 7), bv(0b0000010, 7)),
    bvsmod(bv(0b0010100, 7), bv(0b0000100, 7)),
    bvsmod(bv(0b0001000, 7), bv(0b0001000, 7)),
    bvsmod(bv(0b0010000, 7), bv(0b0010000, 7)),
    bvsmod(bv(0b0100000, 7), bv(0b0100000, 7)),
    bvsmod(bv(0b0000000, 7), bv(0b0000001, 7)),
    bvsmod(bv(0b1000000, 7), bv(0b1000010, 7)),
    bvsmod(bv(0b0000000, 7), bv(0b0000100, 7)),
    bvsmod(bv(0b0100000, 7), bv(0b0000110, 7)),
    bvsmod(bv(0b0010000, 7), bv(0b0000111, 7)),

    bvsrem(bv(0x88888888, 32), bv(0x99999999, 32)),
    bvsrem(bv(0x12345678, 32), bv(0, 32)),
    bvsrem(bv(0x12345678, 32), bv(1, 32)),
    bvsrem(bv(0x12345678, 32), bv(2, 32)),
    bvsrem(bv(0x12345678, 32), bv(3, 32)),
    bvsrem(bv(0x12345678, 32), bv(32, 32)),
    bvsrem(bv(0x12345678, 32), bv(64, 32)),
    bvsrem(bv(0x12345678, 32), bv(0x12345678, 32)),
    bvsrem(bv(0xf2345678, 32), bv(0, 32)),
    bvsrem(bv(0xf2345678, 32), bv(1, 32)),
    bvsrem(bv(0xf2345678, 32), bv(2, 32)),
    bvsrem(bv(0xf2345678, 32), bv(3, 32)),
    bvsrem(bv(0xf2345678, 32), bv(32, 32)),
    bvsrem(bv(0xf2345678, 32), bv(64, 32)),
    bvsrem(bv(0xf2345678, 32), bv(0x12345678, 32)),
    bvsrem(bv(0b10000000, 8), bv(0, 8)),
    bvsrem(bv(0b10000000, 8), bv(1, 8)),
    bvsrem(bv(0b10000000, 8), bv(2, 8)),
    bvsrem(bv(0b10000000, 8), bv(3, 8)),
    bvsrem(bv(0b10000000, 8), bv(4, 8)),
    bvsrem(bv(0b10000000, 8), bv(5, 8)),
    bvsrem(bv(0b10000000, 8), bv(6, 8)),
    bvsrem(bv(0b10000000, 8), bv(7, 8)),
    bvsrem(bv(0b10000000, 8), bv(8, 8)),
    bvsrem(bv(0b10000000, 8), bv(9, 8)),
    bvsrem(bv(0b10000000, 8), bv(123, 8)),
    bvsrem(bv(0b10001000, 8), bv(0, 8)),
    bvsrem(bv(0b10001000, 8), bv(1, 8)),
    bvsrem(bv(0b10001000, 8), bv(2, 8)),
    bvsrem(bv(0b10001000, 8), bv(3, 8)),
    bvsrem(bv(0b10001000, 8), bv(4, 8)),
    bvsrem(bv(0b10001000, 8), bv(5, 8)),
    bvsrem(bv(0b10001000, 8), bv(6, 8)),
    bvsrem(bv(0b10001000, 8), bv(7, 8)),
    bvsrem(bv(0b10001000, 8), bv(8, 8)),
    bvsrem(bv(0b10001000, 8), bv(9, 8)),
    bvsrem(bv(0b10001000, 8), bv(123, 8)),
    bvsrem(bv(0b00010001, 8), bv(0b00000001, 8)),
    bvsrem(bv(0b00010010, 8), bv(0b00000010, 8)),
    bvsrem(bv(0b00010100, 8), bv(0b00000100, 8)),
    bvsrem(bv(0b00001000, 8), bv(0b00001000, 8)),
    bvsrem(bv(0b00010000, 8), bv(0b00010000, 8)),
    bvsrem(bv(0b00100000, 8), bv(0b00100000, 8)),
    bvsrem(bv(0b01000000, 8), bv(0b01000001, 8)),
    bvsrem(bv(0b10000000, 8), bv(0b10000010, 8)),
    bvsrem(bv(0b01000000, 8), bv(0b00000011, 8)),
    bvsrem(bv(0b00100000, 8), bv(0b00000101, 8)),
    bvsrem(bv(0b00010000, 8), bv(0b00000110, 8)),
    bvsrem(bv(0b0010001, 7), bv(0b0000001, 7)),
    bvsrem(bv(0b0010010, 7), bv(0b0000010, 7)),
    bvsrem(bv(0b0010100, 7), bv(0b0000100, 7)),
    bvsrem(bv(0b0001000, 7), bv(0b0001000, 7)),
    bvsrem(bv(0b0010000, 7), bv(0b0010000, 7)),
    bvsrem(bv(0b0100000, 7), bv(0b0100000, 7)),
    bvsrem(bv(0b0000000, 7), bv(0b0000001, 7)),
    bvsrem(bv(0b1000000, 7), bv(0b1000010, 7)),
    bvsrem(bv(0b0000000, 7), bv(0b0000100, 7)),
    bvsrem(bv(0b0100000, 7), bv(0b0000110, 7)),
    bvsrem(bv(0b0010000, 7), bv(0b0000111, 7)),
]

if __name__ == '__main__':
    for test in tests:
        trv = test.evaluate()
        z3v = evaluateAstViaZ3(test)
        if not trv == z3v:
            print '[KO]', test
            print '\tTriton value : %x' %(trv)
            print '\tZ3 value     : %x' %(z3v)
        else:
            print '[OK]', test
    sys.exit(0)

