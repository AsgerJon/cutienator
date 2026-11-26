//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconlabel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconlabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickIconLabel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickIconLabel : QQuickIconLabel {
  using QQuickIconLabel::componentComplete;
  using QQuickIconLabel::geometryChange;
};

//  A QQuickIconLabel that Python can take functions over in. Every QQuickIconLabel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickIconLabelCall0)(const void *, int *);
typedef void (*CuteQQuickIconLabelCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef const QRectF * (*CuteQQuickIconLabelCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickIconLabelCall3)(const void *, int *);
typedef bool (*CuteQQuickIconLabelCall4)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickIconLabelCall5)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickIconLabelCall6)(const void *, int *);
typedef void * (*CuteQQuickIconLabelCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickIconLabelCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIconLabelCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickIconLabelCall10)(const void *, int *);
typedef void (*CuteQQuickIconLabelCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickIconLabelCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickIconLabelCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickIconLabelCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickIconLabelCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickIconLabelCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickIconLabelCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickIconLabelCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickIconLabelCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickIconLabelCall20)(const void *, int *);
typedef void (*CuteQQuickIconLabelCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickIconLabelCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickIconLabelCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickIconLabelCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickIconLabelCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickIconLabelCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickIconLabelCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickIconLabelCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickIconLabelCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickIconLabelCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickIconLabelCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickIconLabelCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickIconLabelCall33)(const void *, int *);
typedef void (*CuteQQuickIconLabelCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickIconLabelCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIconLabelCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIconLabelCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIconLabelCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIconLabelCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIconLabelCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickIconLabel : public QQuickIconLabel {
public:
  using QQuickIconLabel::QQuickIconLabel;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickIconLabel::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickIconLabelCall0 call = reinterpret_cast<CuteQQuickIconLabelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickIconLabel::componentComplete();
  }

  //  void QQuickIconLabel::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickIconLabelCall1 call = reinterpret_cast<CuteQQuickIconLabelCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickIconLabel::geometryChange(newGeometry, oldGeometry);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickIconLabelCall2 call = reinterpret_cast<CuteQQuickIconLabelCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickIconLabelCall3 call = reinterpret_cast<CuteQQuickIconLabelCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickIconLabelCall4 call = reinterpret_cast<CuteQQuickIconLabelCall4>(taken[4]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickIconLabelCall5 call = reinterpret_cast<CuteQQuickIconLabelCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickIconLabelCall6 call = reinterpret_cast<CuteQQuickIconLabelCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickIconLabelCall7 call = reinterpret_cast<CuteQQuickIconLabelCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickIconLabelCall8 call = reinterpret_cast<CuteQQuickIconLabelCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickIconLabelCall9 call = reinterpret_cast<CuteQQuickIconLabelCall9>(taken[9]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickIconLabelCall10 call = reinterpret_cast<CuteQQuickIconLabelCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickIconLabelCall11 call = reinterpret_cast<CuteQQuickIconLabelCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickIconLabelCall12 call = reinterpret_cast<CuteQQuickIconLabelCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickIconLabelCall13 call = reinterpret_cast<CuteQQuickIconLabelCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickIconLabelCall14 call = reinterpret_cast<CuteQQuickIconLabelCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickIconLabelCall15 call = reinterpret_cast<CuteQQuickIconLabelCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickIconLabelCall16 call = reinterpret_cast<CuteQQuickIconLabelCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickIconLabelCall17 call = reinterpret_cast<CuteQQuickIconLabelCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickIconLabelCall18 call = reinterpret_cast<CuteQQuickIconLabelCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickIconLabelCall19 call = reinterpret_cast<CuteQQuickIconLabelCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickIconLabelCall20 call = reinterpret_cast<CuteQQuickIconLabelCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickIconLabelCall21 call = reinterpret_cast<CuteQQuickIconLabelCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickIconLabelCall22 call = reinterpret_cast<CuteQQuickIconLabelCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickIconLabelCall23 call = reinterpret_cast<CuteQQuickIconLabelCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickIconLabelCall24 call = reinterpret_cast<CuteQQuickIconLabelCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickIconLabelCall25 call = reinterpret_cast<CuteQQuickIconLabelCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickIconLabelCall26 call = reinterpret_cast<CuteQQuickIconLabelCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickIconLabelCall27 call = reinterpret_cast<CuteQQuickIconLabelCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickIconLabelCall28 call = reinterpret_cast<CuteQQuickIconLabelCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickIconLabelCall29 call = reinterpret_cast<CuteQQuickIconLabelCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickIconLabelCall30 call = reinterpret_cast<CuteQQuickIconLabelCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickIconLabelCall31 call = reinterpret_cast<CuteQQuickIconLabelCall31>(taken[31]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  QSGNode *QQuickItem::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickIconLabelCall32 call = reinterpret_cast<CuteQQuickIconLabelCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickIconLabelCall33 call = reinterpret_cast<CuteQQuickIconLabelCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickIconLabelCall34 call = reinterpret_cast<CuteQQuickIconLabelCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickIconLabelCall35 call = reinterpret_cast<CuteQQuickIconLabelCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickIconLabelCall36 call = reinterpret_cast<CuteQQuickIconLabelCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickIconLabelCall37 call = reinterpret_cast<CuteQQuickIconLabelCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickIconLabelCall38 call = reinterpret_cast<CuteQQuickIconLabelCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickIconLabelCall39 call = reinterpret_cast<CuteQQuickIconLabelCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickIconLabelCall40 call = reinterpret_cast<CuteQQuickIconLabelCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickIconLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickIconLabel10metaObjectEv(
    const QQuickIconLabel *self) {
  return self->metaObject();
}

//  void *QQuickIconLabel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickIconLabel11qt_metacastEPKc(
    QQuickIconLabel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickIconLabel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickIconLabel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickIconLabel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickIconLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickIconLabel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickIconLabel::tr(s, c, n));
}

//  QQuickIconLabel::QQuickIconLabel(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickIconLabel *ritual_ZN15QQuickIconLabelC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickIconLabel(parent);
}

//  QQuickIconLabel::~QQuickIconLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabelD1Ev(QQuickIconLabel *self) {
  delete self;
}

//  QQuickIcon QQuickIconLabel::icon() const
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZNK15QQuickIconLabel4iconEv(const QQuickIconLabel *self) {
  return new QQuickIcon(self->icon());
}

//  void QQuickIconLabel::setIcon(const QQuickIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel7setIconERK10QQuickIcon(
    QQuickIconLabel *self,
    const QQuickIcon *icon) {
  self->setIcon(*icon);
}

//  QColor QQuickIconLabel::defaultIconColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickIconLabel16defaultIconColorEv(
    const QQuickIconLabel *self) {
  return new QColor(self->defaultIconColor());
}

//  void QQuickIconLabel::setDefaultIconColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel19setDefaultIconColorERK6QColor(
    QQuickIconLabel *self,
    const QColor *color) {
  self->setDefaultIconColor(*color);
}

//  QString QQuickIconLabel::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickIconLabel4textEv(const QQuickIconLabel *self) {
  return new QString(self->text());
}

//  void QQuickIconLabel::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel7setTextERK7QString(
    QQuickIconLabel *self,
    const QString *text) {
  self->setText(*text);
}

//  QFont QQuickIconLabel::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QQuickIconLabel4fontEv(const QQuickIconLabel *self) {
  return new QFont(self->font());
}

//  void QQuickIconLabel::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel7setFontERK5QFont(
    QQuickIconLabel *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QColor QQuickIconLabel::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickIconLabel5colorEv(const QQuickIconLabel *self) {
  return new QColor(self->color());
}

//  void QQuickIconLabel::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel8setColorERK6QColor(
    QQuickIconLabel *self,
    const QColor *color) {
  self->setColor(*color);
}

//  Display QQuickIconLabel::display() const
extern "C" Q_DECL_EXPORT
QQuickIconLabel::Display ritual_ZNK15QQuickIconLabel7displayEv(
    const QQuickIconLabel *self) {
  return self->display();
}

//  void QQuickIconLabel::setDisplay(Display display)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel10setDisplayENS_7DisplayE(
    QQuickIconLabel *self,
    QQuickIconLabel::Display display) {
  self->setDisplay(display);
}

//  qreal QQuickIconLabel::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickIconLabel7spacingEv(const QQuickIconLabel *self) {
  return self->spacing();
}

//  void QQuickIconLabel::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel10setSpacingEd(
    QQuickIconLabel *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  bool QQuickIconLabel::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickIconLabel10isMirroredEv(const QQuickIconLabel *self) {
  return self->isMirrored();
}

//  void QQuickIconLabel::setMirrored(bool mirrored)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel11setMirroredEb(
    QQuickIconLabel *self,
    bool mirrored) {
  self->setMirrored(mirrored);
}

//  Qt::Alignment QQuickIconLabel::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickIconLabel9alignmentEv(const QQuickIconLabel *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QQuickIconLabel::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickIconLabel *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  qreal QQuickIconLabel::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickIconLabel10topPaddingEv(
    const QQuickIconLabel *self) {
  return self->topPadding();
}

//  void QQuickIconLabel::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel13setTopPaddingEd(
    QQuickIconLabel *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  void QQuickIconLabel::resetTopPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel15resetTopPaddingEv(QQuickIconLabel *self) {
  self->resetTopPadding();
}

//  qreal QQuickIconLabel::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickIconLabel11leftPaddingEv(
    const QQuickIconLabel *self) {
  return self->leftPadding();
}

//  void QQuickIconLabel::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel14setLeftPaddingEd(
    QQuickIconLabel *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  void QQuickIconLabel::resetLeftPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel16resetLeftPaddingEv(QQuickIconLabel *self) {
  self->resetLeftPadding();
}

//  qreal QQuickIconLabel::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickIconLabel12rightPaddingEv(
    const QQuickIconLabel *self) {
  return self->rightPadding();
}

//  void QQuickIconLabel::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel15setRightPaddingEd(
    QQuickIconLabel *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  void QQuickIconLabel::resetRightPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel17resetRightPaddingEv(QQuickIconLabel *self) {
  self->resetRightPadding();
}

//  qreal QQuickIconLabel::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickIconLabel13bottomPaddingEv(
    const QQuickIconLabel *self) {
  return self->bottomPadding();
}

//  void QQuickIconLabel::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel16setBottomPaddingEd(
    QQuickIconLabel *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  void QQuickIconLabel::resetBottomPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel18resetBottomPaddingEv(
    QQuickIconLabel *self) {
  self->resetBottomPadding();
}

//  void QQuickIconLabel::defaultIconColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel23defaultIconColorChangedEv(
    QQuickIconLabel *self) {
  self->defaultIconColorChanged();
}

//  QQuickIconLabel::QQuickIconLabel(QQuickIconLabelPrivate &dd, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickIconLabel *ritual_ZN15QQuickIconLabelC1ER22QQuickIconLabelPrivateP10QQuickItem(
    QQuickIconLabelPrivate *dd,
    QQuickItem *parent) {
  return new CuteQQuickIconLabel(*dd, parent);
}

//  void QQuickIconLabel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel17componentCompleteEv(QQuickIconLabel *self) {
  self->componentComplete();
}

//  void QQuickIconLabel::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickIconLabel14geometryChangeERK6QRectFS2_(
    QQuickIconLabel *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QQuickIconLabelPrivate *QQuickIconLabel::d_func()
extern "C" Q_DECL_EXPORT
QQuickIconLabelPrivate *ritual_ZN15QQuickIconLabel6d_funcEv(
    QQuickIconLabel *self) {
  return self->d_func();
}

//  const QQuickIconLabelPrivate *QQuickIconLabel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickIconLabelPrivate *ritual_ZNK15QQuickIconLabel6d_funcEv(
    const QQuickIconLabel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickIconLabel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickIconLabel(
    QQuickIconLabel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickIconLabel *>(self)->take(key, call);
}

//  void QQuickIconLabel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickIconLabel17componentCompleteEv(
    QQuickIconLabel *self) {
  static_cast<OwnQQuickIconLabel *>(self)->OwnQQuickIconLabel::componentComplete();
}

//  void QQuickIconLabel::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickIconLabel14geometryChangeERK6QRectFS2_(
    QQuickIconLabel *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickIconLabel *>(self)->OwnQQuickIconLabel::geometryChange(
      *newGeometry,
      *oldGeometry);
}
