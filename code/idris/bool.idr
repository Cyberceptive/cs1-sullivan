-- total functions
-- block comments
-- symbolic arguments
-- pattern matching: any argument

module bool

data bool = true | false

id: bool -> bool
id b = b

constFalse: bool -> bool
constFalse _ = false

constTrue: bool -> bool
constTrue _ = true

not: bool -> bool
not true = false
not _ = true

