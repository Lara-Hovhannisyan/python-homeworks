class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z


    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    def get_z(self):
        return self._z

    def set_z(self, z):
        self._z = z

    # Unary Operators

    def __neg__(self):
        return Vector3D(-self._x, -self._y, -self._z)

    def __pos__(self):
        return Vector3D(self._x, self._y, self._z)

    def __abs__(self):
        return (self._x ** 2 + self._y ** 2 + self._z ** 2) ** 0.5

    # Comparison Operators

    def __eq__(self, other):
        if isinstance(other, Vector3D):
            return self._x == other.get_x() and self._y == other.get_y() and self._z == other.get_z()
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Vector3D):
            return abs(self) < abs(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vector3D):
            return abs(self) > abs(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Vector3D):
            return abs(self) <= abs(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Vector3D):
            return abs(self) >= abs(other)
        return NotImplemented

    # Binary Arithmetic Operators

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self._x + other.get_x(), self._y + other.get_y(), self._z + other.get_z())
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self._x - other.get_x(), self._y - other.get_y(), self._z - other.get_z())
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(
                self._y * other.get_z() - self._z * other.get_y(),
                self._z * other.get_x() - self._x * other.get_z(),
                self._x * other.get_y() - self._y * other.get_x()
            )
        elif isinstance(other, (int, float)):
            return Vector3D(self._x * other, self._y * other, self._z * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Vector3D(self._x / other, self._y / other, self._z / other)

    def __floordiv__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self._x // other.get_x(), self._y // other.get_y(), self._z // other.get_z())
        return Vector3D(self._x // other, self._y // other, self._z // other)


    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self._x % other, self._y % other, self._z % other)
        return NotImplemented

    def __divmod__(self, other):
        if isinstance(other, (int, float)):
            div, mod = divmod(abs(self), abs(other))
            return div * (self / abs(self)), mod * (self / abs(self))
        return NotImplemented

    def __pow__(self, other, modulo=None):
        if isinstance(other, (int, float)):
            return Vector3D(self._x ** other, self._y ** other, self._z ** other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Vector3D):
            self._x += other._x
            self._y += other._y
            self._z += other._z
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Vector3D):
            self._x -= other._x
            self._y -= other._y
            self._z -= other._z
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self._x *= other
            self._y *= other
            self._z *= other
            return self
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self._x /= other
            self._y /= other
            self._z /= other
            return self
        return NotImplemented

    def __ifloordiv__(self, other):
        if isinstance(other, (int, float)):
            self._x //= other
            self._y //= other
            self._z //= other
            return self
        return NotImplemented

    def __imod__(self, other):
        if isinstance(other, (int, float)):
            self._x %= other
            self._y %= other
            self._z %= other
            return self
        return NotImplemented

    def __ipow__(self, other, modulo=None):
        if isinstance(other, (int, float)):
            self._x **= other
            self._y **= other
            self._z **= other
            return self
        return NotImplemented

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"

    def __repr__(self):
        return f"Vector3D(x={self._x}, y={self._y}, z={self._z})"

    def __format__(self, format_spec):
        formatted_values = [format(coord, format_spec) for coord in [self._x, self._y, self._z]]
        return f"({', '.join(formatted_values)})"

    def __delitem__(self, key):
        raise TypeError("Item deletion is not supported for Vector3D")

    def __contains__(self, item):
        return item in (self._x, self._y, self._z)

    def __len__(self):
        return 3
