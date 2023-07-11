resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.sprints_vpc.id

  tags = {
    Name = var.internet-gateway
  }
}