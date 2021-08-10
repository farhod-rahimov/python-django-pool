def my_var():
	i = 42
	s1 = "42"
	s2 = "quarante-deux"
	f = 42.0
	b = True
	l = [42]
	d = {42:42}
	t = tuple ({42})
	s = set()

	print(f'{i} has a type {i.__class__}')
	print(f'{s1} has a type {s1.__class__}')
	print(f'{s2} has a type {s2.__class__}')
	print(f'{f} has a type {f.__class__}')
	print(f'{b} has a type {b.__class__}')
	print(f'{l} has a type {l.__class__}')
	print(f'{d} has a type {d.__class__}')
	print(f'{t} has a type {t.__class__}')
	print(f'{s} has a type {s.__class__}')

if __name__ == '__main__':
	my_var()