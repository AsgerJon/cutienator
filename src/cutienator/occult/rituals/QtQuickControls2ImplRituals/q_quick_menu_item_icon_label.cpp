//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickmenuitemiconlabel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickmenuitemiconlabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/private/qquickiconlabel_p.h>
#include <QtQuickControls2Impl/private/qquickiconlabel_p_p.h>
#include <QtQuickControls2Impl/private/qquickiconimage_p.h>
#include <QtQuickControls2Impl/private/qquickmnemoniclabel_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtQuickTemplates2/private/qquickicon_p.h>
#include <QtQuickTemplates2/private/qquickicon_p_p.h>
#include <QtQuickControls2Impl/private/qquickiconimage_p.h>
#include <QtQuickControls2Impl/private/qquickmenuitemiconlabel_p.h>
#include <QtQuickControls2Impl/private/qquickmenuitemiconlabel_p_p.h>
#include <QtQuickControls2Impl/private/qquickmnemoniclabel_p.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtQuickTemplates2/private/qquickaction_p.h>
#include <QtQuickTemplates2/private/qquickmenuitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickiconlabel.cpp, line 24, as _ZN22QQuickIconLabelPrivate17completeComponentEP10QQuickItem
inline void QQuickIconLabelPrivate::completeComponent(QQuickItem *item)
{
    if (QQmlParserStatus *parserStatus = qobject_cast<QQmlParserStatus *>(item))
        parserStatus->componentComplete();
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 270, as _ZN23QQuickMenuItemIconLabelD1Ev
inline QQuickMenuItemIconLabel::~QQuickMenuItemIconLabel()
{
    Q_D(QQuickMenuItemIconLabel);
    if (d->shortcutLabel)
        d->unwatchChanges(d->shortcutLabel);
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 282, as _ZNK23QQuickMenuItemIconLabel8menuItemEv
inline QQuickMenuItem *QQuickMenuItemIconLabel::menuItem() const
{
    Q_D(const QQuickMenuItemIconLabel);
    return d->menuItem;
}

//  from ../qtdeclarative/src/quickcontrolsimpl/qquickmenuitemiconlabel.cpp, line 299, as _ZN23QQuickMenuItemIconLabel17componentCompleteEv
inline void QQuickMenuItemIconLabel::componentComplete()
{
    Q_D(QQuickMenuItemIconLabel);
    if (d->shortcutLabel)
        QQuickIconLabelPrivate::completeComponent(d->shortcutLabel);

    QQuickIconLabel::componentComplete();

    // See QQuickIconLabel::componentComplete for why we do this.
    const auto paintOrderChildItems = QQuickItemPrivate::get(this)->paintOrderChildItems();
    const auto bottomMostFosterChildIt = std::find_if(paintOrderChildItems.constBegin(),
        paintOrderChildItems.constEnd(), [d](QQuickItem *item) {
            return item != d->label && item != d->image && item != d->shortcutLabel;
        });
    if (bottomMostFosterChildIt != paintOrderChildItems.constEnd()) {
        const QQuickItem *bottomMostFosterChild = *bottomMostFosterChildIt;
        if (d->shortcutLabel)
            d->shortcutLabel->stackBefore(bottomMostFosterChild);
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickMenuItemIconLabel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMenuItemIconLabel : QQuickMenuItemIconLabel {
  using QQuickMenuItemIconLabel::componentComplete;
};

//  A QQuickMenuItemIconLabel that Python can take functions over in. Every QQuickMenuItemIconLabel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMenuItemIconLabelCall0)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall1)(const void *, const QRectF *, const QRectF *, int *);
typedef const QRectF * (*CuteQQuickMenuItemIconLabelCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickMenuItemIconLabelCall3)(const void *, int *);
typedef bool (*CuteQQuickMenuItemIconLabelCall4)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickMenuItemIconLabelCall5)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickMenuItemIconLabelCall6)(const void *, int *);
typedef void * (*CuteQQuickMenuItemIconLabelCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMenuItemIconLabelCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuItemIconLabelCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall10)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall12)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickMenuItemIconLabelCall13)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickMenuItemIconLabelCall14)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall20)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall21)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMenuItemIconLabelCall22)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickMenuItemIconLabelCall23)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall24)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall26)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuItemIconLabelCall27)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuItemIconLabelCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuItemIconLabelCall29)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickMenuItemIconLabelCall30)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickMenuItemIconLabelCall31)(const void *, QQuickItem *, QEvent *, int *);
typedef void * (*CuteQQuickMenuItemIconLabelCall32)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall33)(const void *, int *);
typedef void (*CuteQQuickMenuItemIconLabelCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickMenuItemIconLabelCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuItemIconLabelCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuItemIconLabelCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuItemIconLabelCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuItemIconLabelCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickMenuItemIconLabelCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickMenuItemIconLabel : public QQuickMenuItemIconLabel {
public:
  using QQuickMenuItemIconLabel::QQuickMenuItemIconLabel;
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

  //  void QQuickMenuItemIconLabel::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall0 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickMenuItemIconLabel::componentComplete();
  }

  //  void QQuickIconLabel::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall1 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickIconLabel::geometryChange(newGeometry, oldGeometry);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall2 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall3 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall4 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall4>(taken[4]);
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
      CuteQQuickMenuItemIconLabelCall5 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall5>(taken[5]);
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
      CuteQQuickMenuItemIconLabelCall6 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall7 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall7>(taken[7]);
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
      CuteQQuickMenuItemIconLabelCall8 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall8>(taken[8]);
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
      CuteQQuickMenuItemIconLabelCall9 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall9>(taken[9]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall10 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall11 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall12 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall12>(taken[12]);
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
      CuteQQuickMenuItemIconLabelCall13 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall13>(taken[13]);
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
      CuteQQuickMenuItemIconLabelCall14 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall15 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall16 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall17 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall18 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall19 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall20 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall21 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall21>(taken[21]);
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
      CuteQQuickMenuItemIconLabelCall22 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall22>(taken[22]);
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
      CuteQQuickMenuItemIconLabelCall23 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall24 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall25 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall26 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall26>(taken[26]);
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
      CuteQQuickMenuItemIconLabelCall27 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall27>(taken[27]);
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
      CuteQQuickMenuItemIconLabelCall28 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall28>(taken[28]);
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
      CuteQQuickMenuItemIconLabelCall29 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall29>(taken[29]);
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
      CuteQQuickMenuItemIconLabelCall30 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall30>(taken[30]);
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
      CuteQQuickMenuItemIconLabelCall31 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall31>(taken[31]);
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
      CuteQQuickMenuItemIconLabelCall32 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall32>(taken[32]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickItem::updatePaintNode(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall33 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickMenuItemIconLabelCall34 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall34>(taken[34]);
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
      CuteQQuickMenuItemIconLabelCall35 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall35>(taken[35]);
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
      CuteQQuickMenuItemIconLabelCall36 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall36>(taken[36]);
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
      CuteQQuickMenuItemIconLabelCall37 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall37>(taken[37]);
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
      CuteQQuickMenuItemIconLabelCall38 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall38>(taken[38]);
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
      CuteQQuickMenuItemIconLabelCall39 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall39>(taken[39]);
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
      CuteQQuickMenuItemIconLabelCall40 call = reinterpret_cast<CuteQQuickMenuItemIconLabelCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickMenuItemIconLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickMenuItemIconLabel10metaObjectEv(
    const QQuickMenuItemIconLabel *self) {
  return self->metaObject();
}

//  QQuickMenuItemIconLabel::~QQuickMenuItemIconLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMenuItemIconLabelD1Ev(QQuickMenuItemIconLabel *self) {
  delete self;
}

//  QQuickMenuItem *QQuickMenuItemIconLabel::menuItem() const
extern "C" Q_DECL_EXPORT
QQuickMenuItem *ritual_ZNK23QQuickMenuItemIconLabel8menuItemEv(
    const QQuickMenuItemIconLabel *self) {
  return self->menuItem();
}

//  void QQuickMenuItemIconLabel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickMenuItemIconLabel17componentCompleteEv(
    QQuickMenuItemIconLabel *self) {
  self->componentComplete();
}

//  QQuickMenuItemIconLabelPrivate *QQuickMenuItemIconLabel::d_func()
extern "C" Q_DECL_EXPORT
QQuickMenuItemIconLabelPrivate *ritual_ZN23QQuickMenuItemIconLabel6d_funcEv(
    QQuickMenuItemIconLabel *self) {
  return self->d_func();
}

//  const QQuickMenuItemIconLabelPrivate *QQuickMenuItemIconLabel::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickMenuItemIconLabelPrivate *ritual_ZNK23QQuickMenuItemIconLabel6d_funcEv(
    const QQuickMenuItemIconLabel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickMenuItemIconLabel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMenuItemIconLabel(
    QQuickMenuItemIconLabel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMenuItemIconLabel *>(self)->take(key, call);
}

//  void QQuickMenuItemIconLabel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuickMenuItemIconLabel17componentCompleteEv(
    QQuickMenuItemIconLabel *self) {
  static_cast<OwnQQuickMenuItemIconLabel *>(self)->OwnQQuickMenuItemIconLabel::componentComplete();
}
