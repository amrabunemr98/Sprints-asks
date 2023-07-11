#Route table of public
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.sprints_vpc.id

  route {
    cidr_block = var.cidr-rt
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = var.tag_public
  }
}

#Resource:route table association for public
resource "aws_route_table_association" "rt_public" {
  subnet_id      = aws_subnet.subnets["public-subnet"].id
  route_table_id = aws_route_table.public_rt.id
}




#Route table of private
resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.sprints_vpc.id

  route {
    cidr_block = var.cidr-rt
    nat_gateway_id = aws_nat_gateway.nat.id
  }

  tags = {
    Name = var.tag_private
  }
}

#Resource:route table association for private
resource "aws_route_table_association" "rt_a" {
  subnet_id      = aws_subnet.subnets["private-subnet"].id
  route_table_id = aws_route_table.private_rt.id
}



