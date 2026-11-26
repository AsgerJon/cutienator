//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyleselector_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtSvg/qtsvgglobal.h>
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#if QT_CONFIG(cssparser)
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyleselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/private/qsvgstyleselector_p.h>
#include <QtSvg/private/qsvgnode_p.h>
#include <QtSvg/private/qsvgstructure_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 17, as _ZN17QSvgStyleSelectorD2Ev
inline QSvgStyleSelector::~QSvgStyleSelector()
{
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 90, as _ZNK17QSvgStyleSelector10isNullNodeEN4QCss13StyleSelector7NodePtrE
inline bool QSvgStyleSelector::isNullNode(NodePtr node) const
{
    return !node.ptr;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 95, as _ZNK17QSvgStyleSelector10parentNodeEN4QCss13StyleSelector7NodePtrE
inline QCss::StyleSelector::NodePtr QSvgStyleSelector::parentNode(NodePtr node) const
{
    QSvgNode *n = svgNode(node);
    NodePtr newNode;
    newNode.ptr = 0;
    newNode.id = 0;
    if (n) {
        QSvgNode *svgParent = n->parent();
        if (svgParent) {
            newNode.ptr = svgParent;
        }
    }
    return newNode;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 127, as _ZNK17QSvgStyleSelector13duplicateNodeEN4QCss13StyleSelector7NodePtrE
inline QCss::StyleSelector::NodePtr QSvgStyleSelector::duplicateNode(NodePtr node) const
{
    NodePtr n;
    n.ptr = node.ptr;
    n.id  = node.id;
    return n;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 65, as _ZNK17QSvgStyleSelector13hasAttributesEN4QCss13StyleSelector7NodePtrE
inline bool QSvgStyleSelector::hasAttributes(NodePtr node) const
{
    QSvgNode *n = svgNode(node);
    return (n &&
            (!n->nodeId().isEmpty() || !n->xmlClass().isEmpty()));
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 53, as _ZNK17QSvgStyleSelector14attributeValueEN4QCss13StyleSelector7NodePtrERKNS0_17AttributeSelectorE
inline QString QSvgStyleSelector::attributeValue(NodePtr node, const QCss::AttributeSelector &asel) const
{
    const QString &name = asel.name;
    QSvgNode *n = svgNode(node);
    if ((!n->nodeId().isEmpty() && (name == QLatin1String("id") ||
                                    name == QLatin1String("xml:id"))))
        return n->nodeId();
    if (!n->xmlClass().isEmpty() && name == QLatin1String("class"))
        return n->xmlClass();
    return QString();
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 45, as _ZNK17QSvgStyleSelector14nodeNameEqualsEN4QCss13StyleSelector7NodePtrERK7QString
inline bool QSvgStyleSelector::nodeNameEquals(NodePtr node, const QString &nodeName) const
{
    QSvgNode *n = svgNode(node);
    if (!n)
        return false;
    return QString::compare(n->typeName(), nodeName, Qt::CaseInsensitive) == 0;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 110, as _ZNK17QSvgStyleSelector19previousSiblingNodeEN4QCss13StyleSelector7NodePtrE
inline QCss::StyleSelector::NodePtr QSvgStyleSelector::previousSiblingNode(NodePtr node) const
{
    NodePtr newNode;
    newNode.ptr = 0;
    newNode.id = 0;

    QSvgNode *n = svgNode(node);
    if (!n)
        return newNode;
    QSvgStructureNode *svgParent = nodeToStructure(n->parent());

    if (svgParent) {
        newNode.ptr = svgParent->previousSiblingNode(n);
    }
    return newNode;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 72, as _ZNK17QSvgStyleSelector7nodeIdsEN4QCss13StyleSelector7NodePtrE
inline QStringList QSvgStyleSelector::nodeIds(NodePtr node) const
{
    QSvgNode *n = svgNode(node);
    QString nid;
    if (n)
        nid = n->nodeId();
    QStringList lst; lst.append(nid);
    return lst;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 135, as _ZNK17QSvgStyleSelector8freeNodeEN4QCss13StyleSelector7NodePtrE
inline void QSvgStyleSelector::freeNode(NodePtr node) const
{
    Q_UNUSED(node);
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 82, as _ZNK17QSvgStyleSelector9nodeNamesEN4QCss13StyleSelector7NodePtrE
inline QStringList QSvgStyleSelector::nodeNames(NodePtr node) const
{
    QSvgNode *n = svgNode(node);
    if (n)
        return QStringList(n->typeName());
    return QStringList();
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 12, as _ZN17QSvgStyleSelectorC1Ev
inline QSvgStyleSelector::QSvgStyleSelector()
{
    nameCaseSensitivity = Qt::CaseInsensitive;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 21, as _ZNK17QSvgStyleSelector7svgNodeEN4QCss13StyleSelector7NodePtrE
inline QSvgNode *QSvgStyleSelector::svgNode(NodePtr node) const
{
    return (QSvgNode*)node.ptr;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 26, as _ZNK17QSvgStyleSelector15nodeToStructureEP8QSvgNode
inline QSvgStructureNode *QSvgStyleSelector::nodeToStructure(QSvgNode *n) const
{
    if (n &&
        (n->type() == QSvgNode::Doc ||
         n->type() == QSvgNode::Group ||
         n->type() == QSvgNode::Defs ||
         n->type() == QSvgNode::Switch)) {
        return (QSvgStructureNode*)n;
    }
    return 0;
}

//  from ../qtsvg/src/svg/css/qsvgstyleselector.cpp, line 38, as _ZNK17QSvgStyleSelector12svgStructureEN4QCss13StyleSelector7NodePtrE
inline QSvgStructureNode *QSvgStyleSelector::svgStructure(NodePtr node) const
{
    QSvgNode *n = svgNode(node);
    QSvgStructureNode *st = nodeToStructure(n);
    return st;
}
//  -----------------------------------------------------------------------

//  A QSvgStyleSelector that Python can take functions over in. Every QSvgStyleSelector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_CSSPARSER)
typedef bool (*CuteQSvgStyleSelectorCall0)(const void *, const QCss::StyleSelector::NodePtr *, const QString *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef QString * (*CuteQSvgStyleSelectorCall1)(const void *, const QCss::StyleSelector::NodePtr *, const QCss::AttributeSelector *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef bool (*CuteQSvgStyleSelectorCall2)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef bool (*CuteQSvgStyleSelectorCall3)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef const QCss::StyleSelector::NodePtr * (*CuteQSvgStyleSelectorCall4)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef const QCss::StyleSelector::NodePtr * (*CuteQSvgStyleSelectorCall5)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef const QCss::StyleSelector::NodePtr * (*CuteQSvgStyleSelectorCall6)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef void (*CuteQSvgStyleSelectorCall7)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
class CuteQSvgStyleSelector : public QSvgStyleSelector {
public:
  using QSvgStyleSelector::QSvgStyleSelector;
  CuteQSvgStyleSelector(const QSvgStyleSelector & other) : QSvgStyleSelector(other) {}
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_CSSPARSER)
    if (!std::strcmp(key, "_ZNK4QCss13StyleSelector14nodeNameEqualsENS0_7NodePtrERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
    if (!std::strcmp(key, "_ZNK4QCss13StyleSelector14attributeValueENS0_7NodePtrERKNS_17AttributeSelectorE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
    if (!std::strcmp(key, "_ZNK4QCss13StyleSelector13hasAttributesENS0_7NodePtrE")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
    if (!std::strcmp(key, "_ZNK4QCss13StyleSelector10isNullNodeENS0_7NodePtrE")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
    if (!std::strcmp(key, "_ZNK4QCss13StyleSelector10parentNodeENS0_7NodePtrE")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
    if (!std::strcmp(key, "_ZNK4QCss13StyleSelector19previousSiblingNodeENS0_7NodePtrE")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
    if (!std::strcmp(key, "_ZNK4QCss13StyleSelector13duplicateNodeENS0_7NodePtrE")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
    if (!std::strcmp(key, "_ZNK4QCss13StyleSelector8freeNodeENS0_7NodePtrE")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_CSSPARSER)
    return false;
  }

#if !defined(QT_NO_CSSPARSER)
  //  bool QSvgStyleSelector::nodeNameEquals(NodePtr node, const QString
  //      &nodeName) const
  bool nodeNameEquals(
      QCss::StyleSelector::NodePtr node,
      const QString &nodeName) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgStyleSelectorCall0 call = reinterpret_cast<CuteQSvgStyleSelectorCall0>(taken[0]);
      bool given = call(this, &node, &nodeName, &handled);
      if (handled) return given;
    }
    return QSvgStyleSelector::nodeNameEquals(node, nodeName);
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  QString QSvgStyleSelector::attributeValue(NodePtr node, const
  //      QCss::AttributeSelector &asel) const
  QString attributeValue(
      QCss::StyleSelector::NodePtr node,
      const QCss::AttributeSelector &asel) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgStyleSelectorCall1 call = reinterpret_cast<CuteQSvgStyleSelectorCall1>(taken[1]);
      QString * given = call(this, &node, &asel, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSvgStyleSelector::attributeValue(node, asel);
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  bool QSvgStyleSelector::hasAttributes(NodePtr node) const
  bool hasAttributes(QCss::StyleSelector::NodePtr node) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgStyleSelectorCall2 call = reinterpret_cast<CuteQSvgStyleSelectorCall2>(taken[2]);
      bool given = call(this, &node, &handled);
      if (handled) return given;
    }
    return QSvgStyleSelector::hasAttributes(node);
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  bool QSvgStyleSelector::isNullNode(NodePtr node) const
  bool isNullNode(QCss::StyleSelector::NodePtr node) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSvgStyleSelectorCall3 call = reinterpret_cast<CuteQSvgStyleSelectorCall3>(taken[3]);
      bool given = call(this, &node, &handled);
      if (handled) return given;
    }
    return QSvgStyleSelector::isNullNode(node);
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  NodePtr QSvgStyleSelector::parentNode(NodePtr node) const
  QCss::StyleSelector::NodePtr parentNode(
      QCss::StyleSelector::NodePtr node) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSvgStyleSelectorCall4 call = reinterpret_cast<CuteQSvgStyleSelectorCall4>(taken[4]);
      const QCss::StyleSelector::NodePtr * given = call(this, &node, &handled);
      if (handled && given) return *given;
    }
    return QSvgStyleSelector::parentNode(node);
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  NodePtr QSvgStyleSelector::previousSiblingNode(NodePtr node) const
  QCss::StyleSelector::NodePtr previousSiblingNode(
      QCss::StyleSelector::NodePtr node) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSvgStyleSelectorCall5 call = reinterpret_cast<CuteQSvgStyleSelectorCall5>(taken[5]);
      const QCss::StyleSelector::NodePtr * given = call(this, &node, &handled);
      if (handled && given) return *given;
    }
    return QSvgStyleSelector::previousSiblingNode(node);
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  NodePtr QSvgStyleSelector::duplicateNode(NodePtr node) const
  QCss::StyleSelector::NodePtr duplicateNode(
      QCss::StyleSelector::NodePtr node) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSvgStyleSelectorCall6 call = reinterpret_cast<CuteQSvgStyleSelectorCall6>(taken[6]);
      const QCss::StyleSelector::NodePtr * given = call(this, &node, &handled);
      if (handled && given) return *given;
    }
    return QSvgStyleSelector::duplicateNode(node);
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  void QSvgStyleSelector::freeNode(NodePtr node) const
  void freeNode(QCss::StyleSelector::NodePtr node) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSvgStyleSelectorCall7 call = reinterpret_cast<CuteQSvgStyleSelectorCall7>(taken[7]);
      call(this, &node, &handled);
      if (handled) return;
    }
    QSvgStyleSelector::freeNode(node);
  }
#endif  // !defined(QT_NO_CSSPARSER)
};

//  QSvgStyleSelector::QSvgStyleSelector()
extern "C" Q_DECL_EXPORT
QSvgStyleSelector *ritual_ZN17QSvgStyleSelectorC1Ev() {
  return new CuteQSvgStyleSelector();
}

//  QSvgStyleSelector::~QSvgStyleSelector()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgStyleSelectorD1Ev(QSvgStyleSelector *self) {
  delete self;
}

//  QSvgNode *QSvgStyleSelector::svgNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QSvgNode *ritual_ZNK17QSvgStyleSelector7svgNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return self->svgNode(*node);
}

//  QSvgStructureNode *QSvgStyleSelector::nodeToStructure(QSvgNode *n) const
extern "C" Q_DECL_EXPORT
QSvgStructureNode *ritual_ZNK17QSvgStyleSelector15nodeToStructureEP8QSvgNode(
    const QSvgStyleSelector *self,
    QSvgNode *n) {
  return self->nodeToStructure(n);
}

//  QSvgStructureNode *QSvgStyleSelector::svgStructure(NodePtr node) const
extern "C" Q_DECL_EXPORT
QSvgStructureNode *ritual_ZNK17QSvgStyleSelector12svgStructureEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return self->svgStructure(*node);
}

//  bool QSvgStyleSelector::nodeNameEquals(NodePtr node, const QString
//      &nodeName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSvgStyleSelector14nodeNameEqualsEN4QCss13StyleSelector7NodePtrERK7QString(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node,
    const QString *nodeName) {
  return self->nodeNameEquals(*node, *nodeName);
}

//  QString QSvgStyleSelector::attributeValue(NodePtr node, const
//      QCss::AttributeSelector &asel) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSvgStyleSelector14attributeValueEN4QCss13StyleSelector7NodePtrERKNS0_17AttributeSelectorE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node,
    const QCss::AttributeSelector *asel) {
  return new QString(self->attributeValue(*node, *asel));
}

//  bool QSvgStyleSelector::hasAttributes(NodePtr node) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSvgStyleSelector13hasAttributesEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return self->hasAttributes(*node);
}

//  QStringList QSvgStyleSelector::nodeIds(NodePtr node) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QSvgStyleSelector7nodeIdsEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QList<QString>(self->nodeIds(*node));
}

//  QStringList QSvgStyleSelector::nodeNames(NodePtr node) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QSvgStyleSelector9nodeNamesEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QList<QString>(self->nodeNames(*node));
}

//  bool QSvgStyleSelector::isNullNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSvgStyleSelector10isNullNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return self->isNullNode(*node);
}

//  NodePtr QSvgStyleSelector::parentNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_ZNK17QSvgStyleSelector10parentNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(self->parentNode(*node));
}

//  NodePtr QSvgStyleSelector::previousSiblingNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_ZNK17QSvgStyleSelector19previousSiblingNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(self->previousSiblingNode(*node));
}

//  NodePtr QSvgStyleSelector::duplicateNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_ZNK17QSvgStyleSelector13duplicateNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(self->duplicateNode(*node));
}

//  void QSvgStyleSelector::freeNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QSvgStyleSelector8freeNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  self->freeNode(*node);
}

//  a Python function taken by a CuteQSvgStyleSelector, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgStyleSelector(
    QSvgStyleSelector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgStyleSelector *>(self)->take(key, call);
}

//  bool QSvgStyleSelector::nodeNameEquals(NodePtr node, const QString
//      &nodeName) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QSvgStyleSelector14nodeNameEqualsEN4QCss13StyleSelector7NodePtrERK7QString(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node,
    const QString *nodeName) {
  return self->QSvgStyleSelector::nodeNameEquals(*node, *nodeName);
}

//  QString QSvgStyleSelector::attributeValue(NodePtr node, const
//      QCss::AttributeSelector &asel) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK17QSvgStyleSelector14attributeValueEN4QCss13StyleSelector7NodePtrERKNS0_17AttributeSelectorE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node,
    const QCss::AttributeSelector *asel) {
  return new QString(self->QSvgStyleSelector::attributeValue(*node, *asel));
}

//  bool QSvgStyleSelector::hasAttributes(NodePtr node) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QSvgStyleSelector13hasAttributesEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return self->QSvgStyleSelector::hasAttributes(*node);
}

//  bool QSvgStyleSelector::isNullNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QSvgStyleSelector10isNullNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return self->QSvgStyleSelector::isNullNode(*node);
}

//  NodePtr QSvgStyleSelector::parentNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_own_ZNK17QSvgStyleSelector10parentNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(
      self->QSvgStyleSelector::parentNode(
          *node));
}

//  NodePtr QSvgStyleSelector::previousSiblingNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_own_ZNK17QSvgStyleSelector19previousSiblingNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(
      self->QSvgStyleSelector::previousSiblingNode(
          *node));
}

//  NodePtr QSvgStyleSelector::duplicateNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_own_ZNK17QSvgStyleSelector13duplicateNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(
      self->QSvgStyleSelector::duplicateNode(
          *node));
}

//  void QSvgStyleSelector::freeNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QSvgStyleSelector8freeNodeEN4QCss13StyleSelector7NodePtrE(
    const QSvgStyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  self->QSvgStyleSelector::freeNode(*node);
}

#endif  // QT_CONFIG(cssparser)
