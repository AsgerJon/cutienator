//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquicktreeviewdelegate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_treeview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktreeviewdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>

//  Only a class built on QQuickTreeViewDelegate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTreeViewDelegate : QQuickTreeViewDelegate {
  using QQuickTreeViewDelegate::defaultFont;
  using QQuickTreeViewDelegate::geometryChange;
  using QQuickTreeViewDelegate::componentComplete;
  using QQuickTreeViewDelegate::mousePressEvent;
};

//  const QMetaObject *QQuickTreeViewDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickTreeViewDelegate10metaObjectEv(
    const QQuickTreeViewDelegate *self) {
  return self->metaObject();
}

//  void *QQuickTreeViewDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickTreeViewDelegate11qt_metacastEPKc(
    QQuickTreeViewDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTreeViewDelegate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickTreeViewDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTreeViewDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTreeViewDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickTreeViewDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTreeViewDelegate::tr(s, c, n));
}

//  QQuickTreeViewDelegate::QQuickTreeViewDelegate(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTreeViewDelegate *ritual_ZN22QQuickTreeViewDelegateC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickTreeViewDelegate(parent);
}

//  qreal QQuickTreeViewDelegate::indentation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTreeViewDelegate11indentationEv(
    const QQuickTreeViewDelegate *self) {
  return self->indentation();
}

//  void QQuickTreeViewDelegate::setIndentation(qreal indentation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate14setIndentationEd(
    QQuickTreeViewDelegate *self,
    qreal indentation) {
  self->setIndentation(indentation);
}

//  bool QQuickTreeViewDelegate::isTreeNode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTreeViewDelegate10isTreeNodeEv(
    const QQuickTreeViewDelegate *self) {
  return self->isTreeNode();
}

//  void QQuickTreeViewDelegate::setIsTreeNode(bool isTreeNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate13setIsTreeNodeEb(
    QQuickTreeViewDelegate *self,
    bool isTreeNode) {
  self->setIsTreeNode(isTreeNode);
}

//  bool QQuickTreeViewDelegate::hasChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTreeViewDelegate11hasChildrenEv(
    const QQuickTreeViewDelegate *self) {
  return self->hasChildren();
}

//  void QQuickTreeViewDelegate::setHasChildren(bool hasChildren)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate14setHasChildrenEb(
    QQuickTreeViewDelegate *self,
    bool hasChildren) {
  self->setHasChildren(hasChildren);
}

//  bool QQuickTreeViewDelegate::expanded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTreeViewDelegate8expandedEv(
    const QQuickTreeViewDelegate *self) {
  return self->expanded();
}

//  void QQuickTreeViewDelegate::setExpanded(bool expanded)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate11setExpandedEb(
    QQuickTreeViewDelegate *self,
    bool expanded) {
  self->setExpanded(expanded);
}

//  bool QQuickTreeViewDelegate::current() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTreeViewDelegate7currentEv(
    const QQuickTreeViewDelegate *self) {
  return self->current();
}

//  void QQuickTreeViewDelegate::setCurrent(bool current)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate10setCurrentEb(
    QQuickTreeViewDelegate *self,
    bool current) {
  self->setCurrent(current);
}

//  bool QQuickTreeViewDelegate::selected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTreeViewDelegate8selectedEv(
    const QQuickTreeViewDelegate *self) {
  return self->selected();
}

//  void QQuickTreeViewDelegate::setSelected(bool selected)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate11setSelectedEb(
    QQuickTreeViewDelegate *self,
    bool selected) {
  self->setSelected(selected);
}

//  bool QQuickTreeViewDelegate::editing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTreeViewDelegate7editingEv(
    const QQuickTreeViewDelegate *self) {
  return self->editing();
}

//  void QQuickTreeViewDelegate::setEditing(bool editing)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate10setEditingEb(
    QQuickTreeViewDelegate *self,
    bool editing) {
  self->setEditing(editing);
}

//  int QQuickTreeViewDelegate::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTreeViewDelegate5depthEv(
    const QQuickTreeViewDelegate *self) {
  return self->depth();
}

//  void QQuickTreeViewDelegate::setDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate8setDepthEi(
    QQuickTreeViewDelegate *self,
    int depth) {
  self->setDepth(depth);
}

//  QQuickTreeView *QQuickTreeViewDelegate::treeView() const
extern "C" Q_DECL_EXPORT
QQuickTreeView *ritual_ZNK22QQuickTreeViewDelegate8treeViewEv(
    const QQuickTreeViewDelegate *self) {
  return self->treeView();
}

//  void QQuickTreeViewDelegate::setTreeView(QQuickTreeView *treeView)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate11setTreeViewEP14QQuickTreeView(
    QQuickTreeViewDelegate *self,
    QQuickTreeView *treeView) {
  self->setTreeView(treeView);
}

//  qreal QQuickTreeViewDelegate::leftMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTreeViewDelegate10leftMarginEv(
    const QQuickTreeViewDelegate *self) {
  return self->leftMargin();
}

//  void QQuickTreeViewDelegate::setLeftMargin(qreal leftMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate13setLeftMarginEd(
    QQuickTreeViewDelegate *self,
    qreal leftMargin) {
  self->setLeftMargin(leftMargin);
}

//  qreal QQuickTreeViewDelegate::rightMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTreeViewDelegate11rightMarginEv(
    const QQuickTreeViewDelegate *self) {
  return self->rightMargin();
}

//  void QQuickTreeViewDelegate::setRightMargin(qreal rightMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate14setRightMarginEd(
    QQuickTreeViewDelegate *self,
    qreal rightMargin) {
  self->setRightMargin(rightMargin);
}

//  void QQuickTreeViewDelegate::indicatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate16indicatorChangedEv(
    QQuickTreeViewDelegate *self) {
  self->indicatorChanged();
}

//  void QQuickTreeViewDelegate::indentationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate18indentationChangedEv(
    QQuickTreeViewDelegate *self) {
  self->indentationChanged();
}

//  void QQuickTreeViewDelegate::isTreeNodeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate17isTreeNodeChangedEv(
    QQuickTreeViewDelegate *self) {
  self->isTreeNodeChanged();
}

//  void QQuickTreeViewDelegate::hasChildrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate18hasChildrenChangedEv(
    QQuickTreeViewDelegate *self) {
  self->hasChildrenChanged();
}

//  void QQuickTreeViewDelegate::expandedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate15expandedChangedEv(
    QQuickTreeViewDelegate *self) {
  self->expandedChanged();
}

//  void QQuickTreeViewDelegate::depthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate12depthChangedEv(
    QQuickTreeViewDelegate *self) {
  self->depthChanged();
}

//  void QQuickTreeViewDelegate::treeviewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate15treeviewChangedEv(
    QQuickTreeViewDelegate *self) {
  self->treeviewChanged();
}

//  void QQuickTreeViewDelegate::leftMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate17leftMarginChangedEv(
    QQuickTreeViewDelegate *self) {
  self->leftMarginChanged();
}

//  void QQuickTreeViewDelegate::rightMarginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate18rightMarginChangedEv(
    QQuickTreeViewDelegate *self) {
  self->rightMarginChanged();
}

//  void QQuickTreeViewDelegate::currentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate14currentChangedEv(
    QQuickTreeViewDelegate *self) {
  self->currentChanged();
}

//  void QQuickTreeViewDelegate::selectedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate15selectedChangedEv(
    QQuickTreeViewDelegate *self) {
  self->selectedChanged();
}

//  void QQuickTreeViewDelegate::editingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate14editingChangedEv(
    QQuickTreeViewDelegate *self) {
  self->editingChanged();
}

//  QFont QQuickTreeViewDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK22QQuickTreeViewDelegate11defaultFontEv(
    const QQuickTreeViewDelegate *self) {
  return new QFont(self->defaultFont());
}

//  void QQuickTreeViewDelegate::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate14geometryChangeERK6QRectFS2_(
    QQuickTreeViewDelegate *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTreeViewDelegate::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate17componentCompleteEv(
    QQuickTreeViewDelegate *self) {
  self->componentComplete();
}

//  void QQuickTreeViewDelegate::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTreeViewDelegate15mousePressEventEP11QMouseEvent(
    QQuickTreeViewDelegate *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  QQuickTreeViewDelegatePrivate *QQuickTreeViewDelegate::d_func()
extern "C" Q_DECL_EXPORT
QQuickTreeViewDelegatePrivate *ritual_ZN22QQuickTreeViewDelegate6d_funcEv(
    QQuickTreeViewDelegate *self) {
  return self->d_func();
}

//  const QQuickTreeViewDelegatePrivate *QQuickTreeViewDelegate::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickTreeViewDelegatePrivate *ritual_ZNK22QQuickTreeViewDelegate6d_funcEv(
    const QQuickTreeViewDelegate *self) {
  return self->d_func();
}

//  QFont QQuickTreeViewDelegate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_own_ZNK22QQuickTreeViewDelegate11defaultFontEv(
    const QQuickTreeViewDelegate *self) {
  return new QFont(
      static_cast<const OwnQQuickTreeViewDelegate *>(self)->OwnQQuickTreeViewDelegate::defaultFont());
}

//  void QQuickTreeViewDelegate::geometryChange(const QRectF &newGeometry,
//      const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTreeViewDelegate14geometryChangeERK6QRectFS2_(
    QQuickTreeViewDelegate *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTreeViewDelegate *>(self)->OwnQQuickTreeViewDelegate::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickTreeViewDelegate::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTreeViewDelegate17componentCompleteEv(
    QQuickTreeViewDelegate *self) {
  static_cast<OwnQQuickTreeViewDelegate *>(self)->OwnQQuickTreeViewDelegate::componentComplete();
}

//  void QQuickTreeViewDelegate::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTreeViewDelegate15mousePressEventEP11QMouseEvent(
    QQuickTreeViewDelegate *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTreeViewDelegate *>(self)->OwnQQuickTreeViewDelegate::mousePressEvent(
      event);
}

#endif  // QT_CONFIG(quick_treeview)
