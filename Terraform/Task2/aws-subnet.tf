resource "aws_subnet" "subnets" {
    for_each = var.sub
  vpc_id            = aws_vpc.sprints_vpc.id
  cidr_block        = each.value.cidr_block
  availability_zone = each.value.availability_zone
  tags = {
    Name = each.value.name
  }
}