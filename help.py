"""
___queries___
"""

# stmt = insert(Product).values(name=name)
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()
#     product_id = result.inserted_primary_key[0]
#     # print(result.keys())
#     return product_id
#
# stmt = select(User).options(selectinload(User.addresses)).order_by(User.id) - OneToMany
# stmt = (
#            select(Address)
#            .options(joinedload(Address.user, innerjoin=True))
#            .order_by(Address.id)
#        ) - ManyTo
#
# stmt = (
#     select(Address)
#     .join(Address.user)
#     .where(User.name == "pkrabs")
#     .options(contains_eager(Address.user))
#     .order_by(Address.id)
# )


# a1 = Address(email_address="pearl.krabs@gmail.com") #  Присвоение по Foreignkey
# u1.addresses.append(a1)

"""
___models___
"""

"""ManyToMany"""

# association_table = Table(
#     "association_table",
#     Base.metadata,
#     Column("left_id", ForeignKey("left_table.id"), primary_key=True),
#     Column("right_id", ForeignKey("right_table.id"), primary_key=True),
# )
#
#
# class Parent(Base):
#     __tablename__ = "left_table"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     children: Mapped[List[Child]] = relationship(
#         secondary=association_table, back_populates="parents"
#     )
#
#
# class Child(Base):
#     __tablename__ = "right_table"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     parents: Mapped[List[Parent]] = relationship(
#         secondary=association_table, back_populates="children"
#     )

"""Delete strings in MTM table"""
# row will be deleted from the "secondary" table
# automatically
# myparent.children.remove(somechild) "or" session.delete(somechild)

"""
Association Proxy
обеспечивает прямой доступ в стиле «многие ко многим» 
между родителем и потомком для трехклассового сопоставления объектов ассоциации."""
# class Parent(Base):
#     __tablename__ = "left_table"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#
#     # many-to-many relationship to Child, bypassing the `Association` class
#     children: Mapped[List["Child"]] = relationship(
#         secondary="association_table", back_populates="parents", viewonly=True
#     )
#
#     # association between Parent -> Association -> Child
#     child_associations: Mapped[List["Association"]] = relationship(
#         back_populates="parent"
#     )
#
#
# class Child(Base):
#     __tablename__ = "right_table"
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#
#     # many-to-many relationship to Parent, bypassing the `Association` class
#     parents: Mapped[List["Parent"]] = relationship(
#         secondary="association_table", back_populates="children", viewonly=True
#     )
#
#     # association between Child -> Association -> Parent
#     parent_associations: Mapped[List["Association"]] = relationship(
#         back_populates="child"
#     )
# p1 = Parent()
# c1 = Child()
# p1.children.append(c1)
