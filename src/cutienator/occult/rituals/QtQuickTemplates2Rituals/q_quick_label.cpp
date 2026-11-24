//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicklabel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicklabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickLabel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabel : QQuickLabel {
  using QQuickLabel::classBegin;
  using QQuickLabel::componentComplete;
  using QQuickLabel::itemChange;
  using QQuickLabel::geometryChange;
  using QQuickLabel::insetChange;
};

//  A QQuickLabel that Python can take functions over in. Every QQuickLabel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLabelCall0)(const void *, int *);
typedef void (*CuteQQuickLabelCall1)(const void *, int *);
typedef void (*CuteQQuickLabelCall2)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickLabelCall3)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickLabelCall4)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef const QRectF * (*CuteQQuickLabelCall5)(const void *, int *);
typedef const QRectF * (*CuteQQuickLabelCall6)(const void *, int *);
typedef void (*CuteQQuickLabelCall7)(const void *, int *);
typedef void (*CuteQQuickLabelCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLabelCall9)(const void *, QMouseEvent *, int *);
typedef void * (*CuteQQuickLabelCall10)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickLabelCall11)(const void *, int *);
typedef void (*CuteQQuickLabelCall12)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickLabelCall13)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickLabelCall14)(const void *, QHoverEvent *, int *);
typedef bool (*CuteQQuickLabelCall15)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickLabelCall16)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickLabelCall17)(const void *, int *);
typedef void * (*CuteQQuickLabelCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabelCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabelCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickLabelCall21)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickLabelCall22)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickLabelCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickLabelCall24)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickLabelCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLabelCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickLabelCall27)(const void *, int *);
typedef void (*CuteQQuickLabelCall28)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickLabelCall29)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickLabelCall30)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLabelCall31)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLabelCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLabelCall33)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickLabelCall34)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickLabelCall35)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickLabelCall36)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabelCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabelCall38)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabelCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabelCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabelCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabelCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLabel : public QQuickLabel {
public:
  using QQuickLabel::QQuickLabel;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QQuickLabel11insetChangeERK9QMarginsFS2_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickTextInterface10invalidateEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[15] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[28] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[36] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickLabel::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLabelCall0 call = reinterpret_cast<CuteQQuickLabelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabel::classBegin();
  }

  //  void QQuickLabel::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabelCall1 call = reinterpret_cast<CuteQQuickLabelCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabel::componentComplete();
  }

  //  void QQuickLabel::itemChange(ItemChange change, const ItemChangeData
  //      &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLabelCall2 call = reinterpret_cast<CuteQQuickLabelCall2>(taken[2]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickLabel::itemChange(change, value);
  }

  //  void QQuickLabel::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLabelCall3 call = reinterpret_cast<CuteQQuickLabelCall3>(taken[3]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickLabel::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickLabel::insetChange(const QMarginsF &newInset, const
  //      QMarginsF &oldInset)
  void insetChange(
      const QMarginsF &newInset,
      const QMarginsF &oldInset) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLabelCall4 call = reinterpret_cast<CuteQQuickLabelCall4>(taken[4]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickLabel::insetChange(newInset, oldInset);
  }

  //  QRectF QQuickText::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLabelCall5 call = reinterpret_cast<CuteQQuickLabelCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickText::boundingRect();
  }

  //  QRectF QQuickText::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLabelCall6 call = reinterpret_cast<CuteQQuickLabelCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickText::clipRect();
  }

  //  void QQuickText::invalidate()
  void invalidate() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickLabelCall7 call = reinterpret_cast<CuteQQuickLabelCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickText::invalidate();
  }

  //  void QQuickText::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickLabelCall8 call = reinterpret_cast<CuteQQuickLabelCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::mousePressEvent(event);
  }

  //  void QQuickText::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickLabelCall9 call = reinterpret_cast<CuteQQuickLabelCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::mouseReleaseEvent(event);
  }

  //  QSGNode *QQuickText::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickLabelCall10 call = reinterpret_cast<CuteQQuickLabelCall10>(taken[10]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickText::updatePaintNode(a0, a1);
  }

  //  void QQuickText::updatePolish()
  void updatePolish() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickLabelCall11 call = reinterpret_cast<CuteQQuickLabelCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickText::updatePolish();
  }

  //  void QQuickText::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickLabelCall12 call = reinterpret_cast<CuteQQuickLabelCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverEnterEvent(event);
  }

  //  void QQuickText::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickLabelCall13 call = reinterpret_cast<CuteQQuickLabelCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverMoveEvent(event);
  }

  //  void QQuickText::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickLabelCall14 call = reinterpret_cast<CuteQQuickLabelCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverLeaveEvent(event);
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickLabelCall15 call = reinterpret_cast<CuteQQuickLabelCall15>(taken[15]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickLabelCall16 call = reinterpret_cast<CuteQQuickLabelCall16>(taken[16]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickLabelCall17 call = reinterpret_cast<CuteQQuickLabelCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickLabelCall18 call = reinterpret_cast<CuteQQuickLabelCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickLabelCall19 call = reinterpret_cast<CuteQQuickLabelCall19>(taken[19]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickLabelCall20 call = reinterpret_cast<CuteQQuickLabelCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickLabelCall21 call = reinterpret_cast<CuteQQuickLabelCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickLabelCall22 call = reinterpret_cast<CuteQQuickLabelCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickLabelCall23 call = reinterpret_cast<CuteQQuickLabelCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickLabelCall24 call = reinterpret_cast<CuteQQuickLabelCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickLabelCall25 call = reinterpret_cast<CuteQQuickLabelCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickLabelCall26 call = reinterpret_cast<CuteQQuickLabelCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickLabelCall27 call = reinterpret_cast<CuteQQuickLabelCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickLabelCall28 call = reinterpret_cast<CuteQQuickLabelCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickLabelCall29 call = reinterpret_cast<CuteQQuickLabelCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickLabelCall30 call = reinterpret_cast<CuteQQuickLabelCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickLabelCall31 call = reinterpret_cast<CuteQQuickLabelCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickLabelCall32 call = reinterpret_cast<CuteQQuickLabelCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickLabelCall33 call = reinterpret_cast<CuteQQuickLabelCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickLabelCall34 call = reinterpret_cast<CuteQQuickLabelCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickLabelCall35 call = reinterpret_cast<CuteQQuickLabelCall35>(taken[35]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickLabelCall36 call = reinterpret_cast<CuteQQuickLabelCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickLabelCall37 call = reinterpret_cast<CuteQQuickLabelCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickLabelCall38 call = reinterpret_cast<CuteQQuickLabelCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickLabelCall39 call = reinterpret_cast<CuteQQuickLabelCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickLabelCall40 call = reinterpret_cast<CuteQQuickLabelCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickLabelCall41 call = reinterpret_cast<CuteQQuickLabelCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickLabelCall42 call = reinterpret_cast<CuteQQuickLabelCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickLabel10metaObjectEv(
    const QQuickLabel *self) {
  return self->metaObject();
}

//  QString QQuickLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickLabel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickLabel::tr(s, c, n));
}

//  QQuickLabel::QQuickLabel(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickLabel *ritual_ZN11QQuickLabelC1EP10QQuickItem(QQuickItem *parent) {
  return new CuteQQuickLabel(parent);
}

//  QQuickLabel::~QQuickLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabelD1Ev(QQuickLabel *self) {
  delete self;
}

//  QFont QQuickLabel::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QQuickLabel4fontEv(const QQuickLabel *self) {
  return new QFont(self->font());
}

//  void QQuickLabel::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel7setFontERK5QFont(
    QQuickLabel *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QQuickItem *QQuickLabel::background() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickLabel10backgroundEv(const QQuickLabel *self) {
  return self->background();
}

//  void QQuickLabel::setBackground(QQuickItem *background)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel13setBackgroundEP10QQuickItem(
    QQuickLabel *self,
    QQuickItem *background) {
  self->setBackground(background);
}

//  qreal QQuickLabel::implicitBackgroundWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickLabel23implicitBackgroundWidthEv(
    const QQuickLabel *self) {
  return self->implicitBackgroundWidth();
}

//  qreal QQuickLabel::implicitBackgroundHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickLabel24implicitBackgroundHeightEv(
    const QQuickLabel *self) {
  return self->implicitBackgroundHeight();
}

//  qreal QQuickLabel::topInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickLabel8topInsetEv(const QQuickLabel *self) {
  return self->topInset();
}

//  void QQuickLabel::setTopInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel11setTopInsetEd(QQuickLabel *self, qreal inset) {
  self->setTopInset(inset);
}

//  void QQuickLabel::resetTopInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel13resetTopInsetEv(QQuickLabel *self) {
  self->resetTopInset();
}

//  qreal QQuickLabel::leftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickLabel9leftInsetEv(const QQuickLabel *self) {
  return self->leftInset();
}

//  void QQuickLabel::setLeftInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel12setLeftInsetEd(QQuickLabel *self, qreal inset) {
  self->setLeftInset(inset);
}

//  void QQuickLabel::resetLeftInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel14resetLeftInsetEv(QQuickLabel *self) {
  self->resetLeftInset();
}

//  qreal QQuickLabel::rightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickLabel10rightInsetEv(const QQuickLabel *self) {
  return self->rightInset();
}

//  void QQuickLabel::setRightInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel13setRightInsetEd(
    QQuickLabel *self,
    qreal inset) {
  self->setRightInset(inset);
}

//  void QQuickLabel::resetRightInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel15resetRightInsetEv(QQuickLabel *self) {
  self->resetRightInset();
}

//  qreal QQuickLabel::bottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickLabel11bottomInsetEv(const QQuickLabel *self) {
  return self->bottomInset();
}

//  void QQuickLabel::setBottomInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel14setBottomInsetEd(
    QQuickLabel *self,
    qreal inset) {
  self->setBottomInset(inset);
}

//  void QQuickLabel::resetBottomInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel16resetBottomInsetEv(QQuickLabel *self) {
  self->resetBottomInset();
}

//  void QQuickLabel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel10classBeginEv(QQuickLabel *self) {
  self->classBegin();
}

//  void QQuickLabel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel17componentCompleteEv(QQuickLabel *self) {
  self->componentComplete();
}

//  void QQuickLabel::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickLabel *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickLabel::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel14geometryChangeERK6QRectFS2_(
    QQuickLabel *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickLabel::insetChange(const QMarginsF &newInset, const QMarginsF
//      &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickLabel11insetChangeERK9QMarginsFS2_(
    QQuickLabel *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  self->insetChange(*newInset, *oldInset);
}

//  QQuickLabelPrivate *QQuickLabel::d_func()
extern "C" Q_DECL_EXPORT
QQuickLabelPrivate *ritual_ZN11QQuickLabel6d_funcEv(QQuickLabel *self) {
  return self->d_func();
}

//  const QQuickLabelPrivate *QQuickLabel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickLabelPrivate *ritual_ZNK11QQuickLabel6d_funcEv(
    const QQuickLabel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickLabel, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabel(
    QQuickLabel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabel *>(self)->take(key, call);
}

//  void QQuickLabel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickLabel10classBeginEv(QQuickLabel *self) {
  static_cast<OwnQQuickLabel *>(self)->OwnQQuickLabel::classBegin();
}

//  void QQuickLabel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickLabel17componentCompleteEv(QQuickLabel *self) {
  static_cast<OwnQQuickLabel *>(self)->OwnQQuickLabel::componentComplete();
}

//  void QQuickLabel::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickLabel10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickLabel *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickLabel *>(self)->OwnQQuickLabel::itemChange(
      change,
      *value);
}

//  void QQuickLabel::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickLabel14geometryChangeERK6QRectFS2_(
    QQuickLabel *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickLabel *>(self)->OwnQQuickLabel::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickLabel::insetChange(const QMarginsF &newInset, const QMarginsF
//      &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QQuickLabel11insetChangeERK9QMarginsFS2_(
    QQuickLabel *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  static_cast<OwnQQuickLabel *>(self)->OwnQQuickLabel::insetChange(
      *newInset,
      *oldInset);
}
