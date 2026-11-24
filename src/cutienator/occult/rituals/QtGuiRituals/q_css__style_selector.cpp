//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_CSSPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCss::StyleSelector that Python can take functions over in. Every QCss::StyleSelector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_CSSPARSER)
typedef bool (*CuteQCss_StyleSelectorCall0)(const void *, const QCss::StyleSelector::NodePtr *, const QString *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef QString * (*CuteQCss_StyleSelectorCall1)(const void *, const QCss::StyleSelector::NodePtr *, const QCss::AttributeSelector *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef bool (*CuteQCss_StyleSelectorCall2)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef bool (*CuteQCss_StyleSelectorCall3)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef const QCss::StyleSelector::NodePtr * (*CuteQCss_StyleSelectorCall4)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef const QCss::StyleSelector::NodePtr * (*CuteQCss_StyleSelectorCall5)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef const QCss::StyleSelector::NodePtr * (*CuteQCss_StyleSelectorCall6)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
#if !defined(QT_NO_CSSPARSER)
typedef void (*CuteQCss_StyleSelectorCall7)(const void *, const QCss::StyleSelector::NodePtr *, int *);
#endif  // !defined(QT_NO_CSSPARSER)
class CuteQCss_StyleSelector : public QCss::StyleSelector {
public:
  using QCss::StyleSelector::StyleSelector;
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
  //  bool QCss::StyleSelector::nodeNameEquals(NodePtr node, const QString
  //      &nodeName) const
  bool nodeNameEquals(
      QCss::StyleSelector::NodePtr node,
      const QString &nodeName) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCss_StyleSelectorCall0 call = reinterpret_cast<CuteQCss_StyleSelectorCall0>(taken[0]);
      bool given = call(this, &node, &nodeName, &handled);
      if (handled) return given;
    }
    return QCss::StyleSelector::nodeNameEquals(node, nodeName);
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  QString QCss::StyleSelector::attributeValue(NodePtr node, const
  //      QCss::AttributeSelector &aSelector) const
  QString attributeValue(
      QCss::StyleSelector::NodePtr node,
      const QCss::AttributeSelector &aSelector) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCss_StyleSelectorCall1 call = reinterpret_cast<CuteQCss_StyleSelectorCall1>(taken[1]);
      QString * given = call(this, &node, &aSelector, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  bool QCss::StyleSelector::hasAttributes(NodePtr node) const
  bool hasAttributes(QCss::StyleSelector::NodePtr node) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQCss_StyleSelectorCall2 call = reinterpret_cast<CuteQCss_StyleSelectorCall2>(taken[2]);
      bool given = call(this, &node, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  bool QCss::StyleSelector::isNullNode(NodePtr node) const
  bool isNullNode(QCss::StyleSelector::NodePtr node) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCss_StyleSelectorCall3 call = reinterpret_cast<CuteQCss_StyleSelectorCall3>(taken[3]);
      bool given = call(this, &node, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  NodePtr QCss::StyleSelector::parentNode(NodePtr node) const
  QCss::StyleSelector::NodePtr parentNode(
      QCss::StyleSelector::NodePtr node) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQCss_StyleSelectorCall4 call = reinterpret_cast<CuteQCss_StyleSelectorCall4>(taken[4]);
      const QCss::StyleSelector::NodePtr * given = call(this, &node, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  NodePtr QCss::StyleSelector::previousSiblingNode(NodePtr node) const
  QCss::StyleSelector::NodePtr previousSiblingNode(
      QCss::StyleSelector::NodePtr node) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQCss_StyleSelectorCall5 call = reinterpret_cast<CuteQCss_StyleSelectorCall5>(taken[5]);
      const QCss::StyleSelector::NodePtr * given = call(this, &node, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  NodePtr QCss::StyleSelector::duplicateNode(NodePtr node) const
  QCss::StyleSelector::NodePtr duplicateNode(
      QCss::StyleSelector::NodePtr node) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQCss_StyleSelectorCall6 call = reinterpret_cast<CuteQCss_StyleSelectorCall6>(taken[6]);
      const QCss::StyleSelector::NodePtr * given = call(this, &node, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // !defined(QT_NO_CSSPARSER)

#if !defined(QT_NO_CSSPARSER)
  //  void QCss::StyleSelector::freeNode(NodePtr node) const
  void freeNode(QCss::StyleSelector::NodePtr node) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCss_StyleSelectorCall7 call = reinterpret_cast<CuteQCss_StyleSelectorCall7>(taken[7]);
      call(this, &node, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_CSSPARSER)
};

//  QCss::StyleSelector::~StyleSelector()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss13StyleSelectorD1Ev(QCss::StyleSelector *self) {
  delete self;
}

//  bool QCss::StyleSelector::nodeNameEquals(NodePtr node, const QString
//      &nodeName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss13StyleSelector14nodeNameEqualsENS0_7NodePtrERK7QString(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node,
    const QString *nodeName) {
  return self->nodeNameEquals(*node, *nodeName);
}

//  QString QCss::StyleSelector::attributeValue(NodePtr node, const
//      QCss::AttributeSelector &aSelector) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QCss13StyleSelector14attributeValueENS0_7NodePtrERKNS_17AttributeSelectorE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node,
    const QCss::AttributeSelector *aSelector) {
  return new QString(self->attributeValue(*node, *aSelector));
}

//  bool QCss::StyleSelector::hasAttributes(NodePtr node) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss13StyleSelector13hasAttributesENS0_7NodePtrE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return self->hasAttributes(*node);
}

//  QStringList QCss::StyleSelector::nodeIds(NodePtr node) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK4QCss13StyleSelector7nodeIdsENS0_7NodePtrE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QList<QString>(self->nodeIds(*node));
}

//  QStringList QCss::StyleSelector::nodeNames(NodePtr node) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK4QCss13StyleSelector9nodeNamesENS0_7NodePtrE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QList<QString>(self->nodeNames(*node));
}

//  bool QCss::StyleSelector::isNullNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss13StyleSelector10isNullNodeENS0_7NodePtrE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return self->isNullNode(*node);
}

//  NodePtr QCss::StyleSelector::parentNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_ZNK4QCss13StyleSelector10parentNodeENS0_7NodePtrE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(self->parentNode(*node));
}

//  NodePtr QCss::StyleSelector::previousSiblingNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_ZNK4QCss13StyleSelector19previousSiblingNodeENS0_7NodePtrE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(self->previousSiblingNode(*node));
}

//  NodePtr QCss::StyleSelector::duplicateNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
QCss::StyleSelector::NodePtr *ritual_ZNK4QCss13StyleSelector13duplicateNodeENS0_7NodePtrE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  return new QCss::StyleSelector::NodePtr(self->duplicateNode(*node));
}

//  void QCss::StyleSelector::freeNode(NodePtr node) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QCss13StyleSelector8freeNodeENS0_7NodePtrE(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node) {
  self->freeNode(*node);
}

//  a Python function taken by a CuteQCss_StyleSelector, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCss_StyleSelector(
    QCss::StyleSelector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCss_StyleSelector *>(self)->take(key, call);
}

//  bool QCss::StyleSelector::nodeNameEquals(NodePtr node, const QString
//      &nodeName) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK4QCss13StyleSelector14nodeNameEqualsENS0_7NodePtrERK7QString(
    const QCss::StyleSelector *self,
    const QCss::StyleSelector::NodePtr *node,
    const QString *nodeName) {
  return self->QCss::StyleSelector::nodeNameEquals(*node, *nodeName);
}

#endif  // !defined(QT_NO_CSSPARSER)
