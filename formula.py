class Element:
    def __init__(self, propositions):
        # 将输入的原子命题字符串分割成列表，并去重
        self.propositions = list(set(propositions.split('v')))
    def __str__(self):
        # 返回元素对象的字符串表示，用析取符号'v'连接原子命题
        return 'v'.join(sorted(self.propositions))

    def merge(self, other):
        # 合并两个Element对象
        if not isinstance(other, Element):
            raise ValueError("Can only merge with another Element")

        # 创建一个新的集合来存储合并后的原子命题
        merged_props = set(self.propositions)
        # 添加另一个Element的原子命题
        merged_props.update(other.propositions)
        # print(merged_props)

        # 创建一个字典来存储原子命题及其否定形式
        negations = {prop: '-' + prop for prop in merged_props if prop.startswith('-')}
        negations.update({'-' + prop: prop for prop in merged_props if not prop.startswith('-')})
        # print(negations)
        # 移除互为反的原子命题
        for prop, neg in negations.items():
            if prop in merged_props and neg in merged_props:

                merged_props.remove(prop)
                merged_props.remove(neg)

        # 特殊情况处理：如果合并后没有原子命题，则返回"contradiction"
        if not merged_props:
            return "contradiction"

        # 创建并返回新的Element对象
        return Element('v'.join(sorted(merged_props)))

class Formula:
    def __init__(self, element_list, target = None):
        self.elements = element_list
        self.target = target

    def __str__(self):
        # 将elements列表中的每个元素转换为字符串，并用逗号分隔
        elements_str = ', '.join(str(element) for element in self.elements)
        # 如果有target，则将其添加到字符串的末尾
        if self.target is not None:
            return f"{elements_str} => {self.target}"
        else:
            return f"[{elements_str}] => None"

    def merge_and_append(self, pair):
        merged_element = self.elements[pair[0]].merge(self.elements[pair[1]])
        self.elements.append(merged_element)

# # 示例使用


# element3 = Element("-AvB")
# element4 = Element("-Bv-C")
# merged_element = element3.merge(element4)
# print(merged_element)
#
# element5 = Element("B")
# element6 = Element("-C")
# merged_element = element5.merge(element6)
# print(merged_element)  # 输出: contradiction
#
# element1 = Element("-A")
# element2 = Element("AvB")
# element_list = [element1, element2]
# formula = Formula(element_list, "B")
# print(formula)
# pair = (0, 1)
# formula.merge_and_append(pair)
# print(formula)
