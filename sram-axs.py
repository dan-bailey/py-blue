import simplepyble

# choose adapter
adapters = simplepyble.Adapter.get_adapters()
adapter = adapters[0]

# build list of nearby BTLE items
