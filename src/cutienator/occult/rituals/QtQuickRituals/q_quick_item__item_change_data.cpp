//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>

//  QQuickItem::ItemChangeData::ItemChangeData(QQuickItem *v)
extern "C" Q_DECL_EXPORT
QQuickItem::ItemChangeData *ritual_ZN10QQuickItem14ItemChangeDataC1EPS_(
    QQuickItem *v) {
  return new QQuickItem::ItemChangeData(v);
}

//  QQuickItem::ItemChangeData::ItemChangeData(QQuickWindow *v)
extern "C" Q_DECL_EXPORT
QQuickItem::ItemChangeData *ritual_ZN10QQuickItem14ItemChangeDataC1EP12QQuickWindow(
    QQuickWindow *v) {
  return new QQuickItem::ItemChangeData(v);
}

//  QQuickItem::ItemChangeData::ItemChangeData(qreal v)
extern "C" Q_DECL_EXPORT
QQuickItem::ItemChangeData *ritual_ZN10QQuickItem14ItemChangeDataC1Ed(
    qreal v) {
  return new QQuickItem::ItemChangeData(v);
}

//  QQuickItem::ItemChangeData::ItemChangeData(bool v)
extern "C" Q_DECL_EXPORT
QQuickItem::ItemChangeData *ritual_ZN10QQuickItem14ItemChangeDataC1Eb(
    bool v) {
  return new QQuickItem::ItemChangeData(v);
}

//  QQuickItem::ItemChangeData::~ItemChangeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQuickItem14ItemChangeDataD1Ev(
    QQuickItem::ItemChangeData *self) {
  delete self;
}
