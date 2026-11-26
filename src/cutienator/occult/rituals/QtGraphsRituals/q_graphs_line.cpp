//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qgraphstheme.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qgraphstheme.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>

//  QVariant QGraphsLine::create(const QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN11QGraphsLine6createERK8QJSValue(const QJSValue *params) {
  return new QVariant(QGraphsLine::create(*params));
}

//  QGraphsLine::QGraphsLine()
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZN11QGraphsLineC1Ev() {
  return new QGraphsLine();
}

//  QGraphsLine::QGraphsLine(const QGraphsLine &other)
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZN11QGraphsLineC1ERKS_(const QGraphsLine *other) {
  return new QGraphsLine(*other);
}

//  QGraphsLine::QGraphsLine(QGraphsLine &&other)
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZN11QGraphsLineC1EOS_(QGraphsLine *other) {
  return new QGraphsLine(std::move(*other));
}

//  QGraphsLine::~QGraphsLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsLineD1Ev(QGraphsLine *self) {
  delete self;
}

//  QGraphsLine &QGraphsLine::operator=(const QGraphsLine &other)
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZN11QGraphsLineaSERKS_(
    QGraphsLine *self,
    const QGraphsLine *other) {
  return &(self->operator=(*other));
}

//  void QGraphsLine::swap(QGraphsLine &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsLine4swapERS_(QGraphsLine *self, QGraphsLine *other) {
  self->swap(*other);
}

//  QGraphsLine &QGraphsLine::operator=(QGraphsLine &&other)
extern "C" Q_DECL_EXPORT
QGraphsLine *ritual_ZN11QGraphsLineaSEOS_(
    QGraphsLine *self,
    QGraphsLine *other) {
  return &(self->operator=(std::move(*other)));
}

//  QColor QGraphsLine::mainColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QGraphsLine9mainColorEv(const QGraphsLine *self) {
  return new QColor(self->mainColor());
}

//  void QGraphsLine::setMainColor(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsLine12setMainColorE6QColor(
    QGraphsLine *self,
    const QColor *newColor) {
  self->setMainColor(*newColor);
}

//  QColor QGraphsLine::subColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QGraphsLine8subColorEv(const QGraphsLine *self) {
  return new QColor(self->subColor());
}

//  void QGraphsLine::setSubColor(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsLine11setSubColorE6QColor(
    QGraphsLine *self,
    const QColor *newColor) {
  self->setSubColor(*newColor);
}

//  qreal QGraphsLine::mainWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsLine9mainWidthEv(const QGraphsLine *self) {
  return self->mainWidth();
}

//  void QGraphsLine::setMainWidth(qreal newWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsLine12setMainWidthEd(
    QGraphsLine *self,
    qreal newWidth) {
  self->setMainWidth(newWidth);
}

//  qreal QGraphsLine::subWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QGraphsLine8subWidthEv(const QGraphsLine *self) {
  return self->subWidth();
}

//  void QGraphsLine::setSubWidth(qreal newWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsLine11setSubWidthEd(
    QGraphsLine *self,
    qreal newWidth) {
  self->setSubWidth(newWidth);
}

//  QColor QGraphsLine::labelTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QGraphsLine14labelTextColorEv(const QGraphsLine *self) {
  return new QColor(self->labelTextColor());
}

//  void QGraphsLine::setLabelTextColor(QColor newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsLine17setLabelTextColorE6QColor(
    QGraphsLine *self,
    const QColor *newColor) {
  self->setLabelTextColor(*newColor);
}

//  void QGraphsLine::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGraphsLine6detachEv(QGraphsLine *self) {
  self->detach();
}

//  QVariant QGraphsLine::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QGraphsLinecv8QVariantEv(const QGraphsLine *self) {
  return new QVariant(self->operator QVariant());
}

//  bool operator==(const QGraphsLine &lhs, const QGraphsLine &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QGraphsLineS1_(
    const QGraphsLine *lhs,
    const QGraphsLine *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGraphsLine &lhs, const QGraphsLine &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QGraphsLineS1_(
    const QGraphsLine *lhs,
    const QGraphsLine *rhs) {
  return operator!=(*lhs, *rhs);
}
