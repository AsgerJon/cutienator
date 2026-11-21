//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayoutitem.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  QWidgetItem::QWidgetItem(QWidget *w)
extern "C" Q_DECL_EXPORT
QWidgetItem *ritual_ZN11QWidgetItemC1EP7QWidget(QWidget *w) {
  return new QWidgetItem(w);
}

//  QWidgetItem::~QWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWidgetItemD1Ev(QWidgetItem *self) {
  delete self;
}

//  QSize QWidgetItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QWidgetItem8sizeHintEv(const QWidgetItem *self) {
  return new QSize(self->sizeHint());
}

//  QSize QWidgetItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QWidgetItem11minimumSizeEv(const QWidgetItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QWidgetItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QWidgetItem11maximumSizeEv(const QWidgetItem *self) {
  return new QSize(self->maximumSize());
}

//  Qt::Orientations QWidgetItem::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWidgetItem19expandingDirectionsEv(const QWidgetItem *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  bool QWidgetItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWidgetItem7isEmptyEv(const QWidgetItem *self) {
  return self->isEmpty();
}

//  void QWidgetItem::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWidgetItem11setGeometryERK5QRect(
    QWidgetItem *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QRect QWidgetItem::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QWidgetItem8geometryEv(const QWidgetItem *self) {
  return new QRect(self->geometry());
}

//  QWidget *QWidgetItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QWidgetItem6widgetEv(const QWidgetItem *self) {
  return self->widget();
}

//  bool QWidgetItem::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWidgetItem17hasHeightForWidthEv(const QWidgetItem *self) {
  return self->hasHeightForWidth();
}

//  int QWidgetItem::heightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWidgetItem14heightForWidthEi(
    const QWidgetItem *self,
    int a0) {
  return self->heightForWidth(a0);
}

//  int QWidgetItem::minimumHeightForWidth(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWidgetItem21minimumHeightForWidthEi(
    const QWidgetItem *self,
    int a0) {
  return self->minimumHeightForWidth(a0);
}

//  QSizePolicy::ControlTypes QWidgetItem::controlTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWidgetItem12controlTypesEv(const QWidgetItem *self) {
  return static_cast<int>(self->controlTypes().toInt());
}
