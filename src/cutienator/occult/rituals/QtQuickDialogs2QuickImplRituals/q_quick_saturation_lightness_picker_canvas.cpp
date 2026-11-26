//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksaturationlightn
//  esspicker_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksaturationlightnesspicker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>

//  Only a class built on QQuickSaturationLightnessPickerCanvas may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSaturationLightnessPickerCanvas : QQuickSaturationLightnessPickerCanvas {
  using QQuickSaturationLightnessPickerCanvas::updatePaintNode;
};

//  const QMetaObject *QQuickSaturationLightnessPickerCanvas::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK37QQuickSaturationLightnessPickerCanvas10metaObjectEv(
    const QQuickSaturationLightnessPickerCanvas *self) {
  return self->metaObject();
}

//  void *QQuickSaturationLightnessPickerCanvas::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN37QQuickSaturationLightnessPickerCanvas11qt_metacastEPKc(
    QQuickSaturationLightnessPickerCanvas *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSaturationLightnessPickerCanvas::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN37QQuickSaturationLightnessPickerCanvas11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSaturationLightnessPickerCanvas *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSaturationLightnessPickerCanvas::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN37QQuickSaturationLightnessPickerCanvas2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSaturationLightnessPickerCanvas::tr(s, c, n));
}

//  QQuickSaturationLightnessPickerCanvas::QQuickSaturationLightnessPickerCan
//      vas(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSaturationLightnessPickerCanvas *ritual_ZN37QQuickSaturationLightnessPickerCanvasC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickSaturationLightnessPickerCanvas(parent);
}

//  qreal QQuickSaturationLightnessPickerCanvas::hue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK37QQuickSaturationLightnessPickerCanvas3hueEv(
    const QQuickSaturationLightnessPickerCanvas *self) {
  return self->hue();
}

//  void QQuickSaturationLightnessPickerCanvas::setHue(qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QQuickSaturationLightnessPickerCanvas6setHueEd(
    QQuickSaturationLightnessPickerCanvas *self,
    qreal h) {
  self->setHue(h);
}

//  void QQuickSaturationLightnessPickerCanvas::hueChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QQuickSaturationLightnessPickerCanvas10hueChangedEv(
    QQuickSaturationLightnessPickerCanvas *self) {
  self->hueChanged();
}

//  QSGNode *QQuickSaturationLightnessPickerCanvas::updatePaintNode(QSGNode
//      *oldNode, UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN37QQuickSaturationLightnessPickerCanvas15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickSaturationLightnessPickerCanvas *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}

//  QImage QQuickSaturationLightnessPickerCanvas::generateImage(int width,
//      int height, double hue01) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK37QQuickSaturationLightnessPickerCanvas13generateImageEiid(
    const QQuickSaturationLightnessPickerCanvas *self,
    int width,
    int height,
    double hue01) {
  return new QImage(self->generateImage(width, height, hue01));
}

//  QSGNode *QQuickSaturationLightnessPickerCanvas::updatePaintNode(QSGNode
//      *oldNode, UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN37QQuickSaturationLightnessPickerCanvas15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickSaturationLightnessPickerCanvas *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickSaturationLightnessPickerCanvas *>(self)->OwnQQuickSaturationLightnessPickerCanvas::updatePaintNode(
      oldNode,
      a1);
}
