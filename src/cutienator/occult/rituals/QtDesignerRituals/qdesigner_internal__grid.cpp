//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/grid_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/grid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  qdesigner_internal::Grid::Grid()
extern "C" Q_DECL_EXPORT
qdesigner_internal::Grid *ritual_ZN18qdesigner_internal4GridC1Ev() {
  return new qdesigner_internal::Grid();
}

//  bool qdesigner_internal::Grid::fromVariantMap(const QVariantMap &vm)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal4Grid14fromVariantMapERK4QMapI7QString8QVariantE(
    qdesigner_internal::Grid *self,
    const QMap<QString, QVariant> *vm) {
  return self->fromVariantMap(*vm);
}

//  void qdesigner_internal::Grid::addToVariantMap(QVariantMap &vm, bool
//      forceKeys) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal4Grid15addToVariantMapER4QMapI7QString8QVariantEb(
    const qdesigner_internal::Grid *self,
    QVariantMap *vm,
    bool forceKeys) {
  self->addToVariantMap(*vm, forceKeys);
}

//  QVariantMap qdesigner_internal::Grid::toVariantMap(bool forceKeys) const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK18qdesigner_internal4Grid12toVariantMapEb(
    const qdesigner_internal::Grid *self,
    bool forceKeys) {
  return new QMap<QString, QVariant>(self->toVariantMap(forceKeys));
}

//  bool qdesigner_internal::Grid::visible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal4Grid7visibleEv(
    const qdesigner_internal::Grid *self) {
  return self->visible();
}

//  void qdesigner_internal::Grid::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal4Grid10setVisibleEb(
    qdesigner_internal::Grid *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool qdesigner_internal::Grid::snapX() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal4Grid5snapXEv(
    const qdesigner_internal::Grid *self) {
  return self->snapX();
}

//  void qdesigner_internal::Grid::setSnapX(bool snap)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal4Grid8setSnapXEb(
    qdesigner_internal::Grid *self,
    bool snap) {
  self->setSnapX(snap);
}

//  bool qdesigner_internal::Grid::snapY() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal4Grid5snapYEv(
    const qdesigner_internal::Grid *self) {
  return self->snapY();
}

//  void qdesigner_internal::Grid::setSnapY(bool snap)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal4Grid8setSnapYEb(
    qdesigner_internal::Grid *self,
    bool snap) {
  self->setSnapY(snap);
}

//  int qdesigner_internal::Grid::deltaX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal4Grid6deltaXEv(
    const qdesigner_internal::Grid *self) {
  return self->deltaX();
}

//  void qdesigner_internal::Grid::setDeltaX(int dx)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal4Grid9setDeltaXEi(
    qdesigner_internal::Grid *self,
    int dx) {
  self->setDeltaX(dx);
}

//  int qdesigner_internal::Grid::deltaY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal4Grid6deltaYEv(
    const qdesigner_internal::Grid *self) {
  return self->deltaY();
}

//  void qdesigner_internal::Grid::setDeltaY(int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal4Grid9setDeltaYEi(
    qdesigner_internal::Grid *self,
    int dy) {
  self->setDeltaY(dy);
}

//  void qdesigner_internal::Grid::paint(QWidget *widget, QPaintEvent *e)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal4Grid5paintEP7QWidgetP11QPaintEvent(
    const qdesigner_internal::Grid *self,
    QWidget *widget,
    QPaintEvent *e) {
  self->paint(widget, e);
}

//  void qdesigner_internal::Grid::paint(QPainter &p, const QWidget *widget,
//      QPaintEvent *e) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal4Grid5paintER8QPainterPK7QWidgetP11QPaintEvent(
    const qdesigner_internal::Grid *self,
    QPainter *p,
    const QWidget *widget,
    QPaintEvent *e) {
  self->paint(*p, widget, e);
}

//  QPoint qdesigner_internal::Grid::snapPoint(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK18qdesigner_internal4Grid9snapPointERK6QPoint(
    const qdesigner_internal::Grid *self,
    const QPoint *p) {
  return new QPoint(self->snapPoint(*p));
}

//  int qdesigner_internal::Grid::widgetHandleAdjustX(int x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal4Grid19widgetHandleAdjustXEi(
    const qdesigner_internal::Grid *self,
    int x) {
  return self->widgetHandleAdjustX(x);
}

//  int qdesigner_internal::Grid::widgetHandleAdjustY(int y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal4Grid19widgetHandleAdjustYEi(
    const qdesigner_internal::Grid *self,
    int y) {
  return self->widgetHandleAdjustY(y);
}

//  bool operator==(const Grid &lhs, const Grid &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_4GridES2_(
    const qdesigner_internal::Grid *lhs,
    const qdesigner_internal::Grid *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Grid &lhs, const Grid &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_4GridES2_(
    const qdesigner_internal::Grid *lhs,
    const qdesigner_internal::Grid *rhs) {
  return operator!=(*lhs, *rhs);
}

//  int qdesigner_internal::Grid::snapValue(int value, int grid) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal4Grid9snapValueEii(
    const qdesigner_internal::Grid *self,
    int value,
    int grid) {
  return self->snapValue(value, grid);
}

//  qdesigner_internal::Grid::~Grid()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal4GridD1Ev(qdesigner_internal::Grid *self) {
  delete self;
}
