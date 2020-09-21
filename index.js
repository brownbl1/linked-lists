const buildNode = (number) => ({ number, next: null })

const printNode = (node) => {
  console.log(`node: ${node.number}`)
  if (node.next) printNode(node.next)
}

const buildNodes = (start, end) => {
  const n = buildNode(start)
  if (start !== end) n.next = buildNodes(start + 1, end)
  return n
}

printNode(buildNodes(1, 5))
