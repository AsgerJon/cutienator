//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlayoutitem.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtWidgets/qsizepolicy.h>

//  QSpacerItem::QSpacerItem(int w, int h, QSizePolicy::Policy hData,
//      QSizePolicy::Policy vData)
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_ZN11QSpacerItemC1EiiN11QSizePolicy6PolicyES1_(
    int w,
    int h,
    QSizePolicy::Policy hData,
    QSizePolicy::Policy vData) {
  return new QSpacerItem(w, h, hData, vData);
}

//  QSpacerItem::~QSpacerItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSpacerItemD1Ev(QSpacerItem *self) {
  delete self;
}

//  void QSpacerItem::changeSize(int w, int h, QSizePolicy::Policy hData,
//      QSizePolicy::Policy vData)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSpacerItem10changeSizeEiiN11QSizePolicy6PolicyES1_(
    QSpacerItem *self,
    int w,
    int h,
    QSizePolicy::Policy hData,
    QSizePolicy::Policy vData) {
  self->changeSize(w, h, hData, vData);
}

//  QSize QSpacerItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QSpacerItem8sizeHintEv(const QSpacerItem *self) {
  return new QSize(self->sizeHint());
}

//  QSize QSpacerItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QSpacerItem11minimumSizeEv(const QSpacerItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QSpacerItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QSpacerItem11maximumSizeEv(const QSpacerItem *self) {
  return new QSize(self->maximumSize());
}

//  Qt::Orientations QSpacerItem::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSpacerItem19expandingDirectionsEv(const QSpacerItem *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  bool QSpacerItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSpacerItem7isEmptyEv(const QSpacerItem *self) {
  return self->isEmpty();
}

//  void QSpacerItem::setGeometry(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSpacerItem11setGeometryERK5QRect(
    QSpacerItem *self,
    const QRect *a0) {
  self->setGeometry(*a0);
}

//  QRect QSpacerItem::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QSpacerItem8geometryEv(const QSpacerItem *self) {
  return new QRect(self->geometry());
}

//  QSpacerItem *QSpacerItem::spacerItem()
extern "C" Q_DECL_EXPORT
QSpacerItem *ritual_ZN11QSpacerItem10spacerItemEv(QSpacerItem *self) {
  return self->spacerItem();
}

//  QSizePolicy QSpacerItem::sizePolicy() const
extern "C" Q_DECL_EXPORT
QSizePolicy *ritual_ZNK11QSpacerItem10sizePolicyEv(const QSpacerItem *self) {
  return new QSizePolicy(self->sizePolicy());
}
