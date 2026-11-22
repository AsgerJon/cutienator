//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayoutitem.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  QLayoutItem::~QLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLayoutItemD1Ev(QLayoutItem *self) {
  delete self;
}

//  QSize QLayoutItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QLayoutItem8sizeHintEv(const QLayoutItem *self) {
  return new QSize(self->sizeHint());
}

//  QSize QLayoutItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QLayoutItem11minimumSizeEv(const QLayoutItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QLayoutItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QLayoutItem11maximumSizeEv(const QLayoutItem *self) {
  return new QSize(self->maximumSize());
}

//  Qt::Orientations QLayoutItem::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem19expandingDirectionsEv(const QLayoutItem *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QLayoutItem::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLayoutItem11setGeometryERK5QRect(
    QLayoutItem *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QRect QLayoutItem::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QLayoutItem8geometryEv(const QLayoutItem *self) {
  return new QRect(self->geometry());
}

//  bool QLayoutItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLayoutItem7isEmptyEv(const QLayoutItem *self) {
  return self->isEmpty();
}

//  bool QLayoutItem::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLayoutItem17hasHeightForWidthEv(const QLayoutItem *self) {
  return self->hasHeightForWidth();
}

//  int QLayoutItem::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem14heightForWidthEi(
    const QLayoutItem *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  int QLayoutItem::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem21minimumHeightForWidthEi(
    const QLayoutItem *self,
    int a0) {
  return self->minimumHeightForWidth(a0);
}

//  void QLayoutItem::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLayoutItem10invalidateEv(QLayoutItem *self) {
  self->invalidate();
}

//  QWidget *QLayoutItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QLayoutItem6widgetEv(const QLayoutItem *self) {
  return self->widget();
}

//  QLayout *QLayoutItem::layout()
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZN11QLayoutItem6layoutEv(QLayoutItem *self) {
  return self->layout();
}

//  QSpacerItem *QLayoutItem::spacerItem()
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_ZN11QLayoutItem10spacerItemEv(QLayoutItem *self) {
  return self->spacerItem();
}

//  Qt::Alignment QLayoutItem::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem9alignmentEv(const QLayoutItem *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QLayoutItem::setAlignment(Qt::Alignment a)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLayoutItem12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QLayoutItem *self,
    int a) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(a));
}

//  QSizePolicy::ControlTypes QLayoutItem::controlTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLayoutItem12controlTypesEv(const QLayoutItem *self) {
  return static_cast<int>(self->controlTypes().toInt());
}
