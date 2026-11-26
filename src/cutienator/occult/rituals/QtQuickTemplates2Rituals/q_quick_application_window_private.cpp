//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickapplicationwindow_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  A QQuickApplicationWindowPrivate that Python can take functions over in. Every QQuickApplicationWindowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickApplicationWindowPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall3)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickApplicationWindowPrivateCall4)(const void *, int *);
typedef const QPalette * (*CuteQQuickApplicationWindowPrivateCall5)(const void *, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall6)(const void *, const QPalette *, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall7)(const void *, QQuickPalette *, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall9)(const void *, int, int, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall10)(const void *, QMouseEvent *, int *);
typedef void * (*CuteQQuickApplicationWindowPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickApplicationWindowPrivateCall12)(const void *, bool, int *);
typedef const QRectF * (*CuteQQuickApplicationWindowPrivateCall13)(const void *, const QRectF *, int *);
typedef bool (*CuteQQuickApplicationWindowPrivateCall14)(const void *, int *);
typedef bool (*CuteQQuickApplicationWindowPrivateCall15)(const void *, int *);
class CuteQQuickApplicationWindowPrivate : public QQuickApplicationWindowPrivate {
public:
  using QQuickApplicationWindowPrivate::QQuickApplicationWindowPrivate;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN30QQuickApplicationWindowPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickApplicationWindowPrivate21itemVisibilityChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickApplicationWindowPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickApplicationWindowPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate13windowPaletteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK30QQuickApplicationWindowPrivate14defaultPaletteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QPalette")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16clearFocusObjectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate13eventReceiverEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate10setVisibleEb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate30participatesInLastWindowClosedEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate14treatAsVisibleEv")) {
      taken[15] = call;
      return true;
    }
    return false;
  }

  //  void QQuickApplicationWindowPrivate::itemGeometryChanged(QQuickItem
  //      *item, QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall0 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall0>(taken[0]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickApplicationWindowPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickApplicationWindowPrivate::itemVisibilityChanged(QQuickItem
  //      *item)
  void itemVisibilityChanged(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall1 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickApplicationWindowPrivate::itemVisibilityChanged(item);
  }

  //  void
  //      QQuickApplicationWindowPrivate::itemImplicitWidthChanged(QQuickIt
  //      em *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall2 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickApplicationWindowPrivate::itemImplicitWidthChanged(item);
  }

  //  void
  //      QQuickApplicationWindowPrivate::itemImplicitHeightChanged(QQuickI
  //      tem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall3 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickApplicationWindowPrivate::itemImplicitHeightChanged(item);
  }

  //  QPalette QQuickApplicationWindowPrivate::windowPalette() const
  QPalette windowPalette() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall4 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall4>(taken[4]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickApplicationWindowPrivate::windowPalette();
  }

  //  QPalette QQuickApplicationWindowPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall5 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall5>(taken[5]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickApplicationWindowPrivate::defaultPalette();
  }

  //  void QQuickApplicationWindowPrivate::updateChildrenPalettes(const
  //      QPalette &parentPalette)
  void updateChildrenPalettes(const QPalette &parentPalette) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall6 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall6>(taken[6]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickApplicationWindowPrivate::updateChildrenPalettes(parentPalette);
  }

  //  void QQuickWindowPrivate::setPalette(QQuickPalette *p)
  void setPalette(QQuickPalette *p) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall7 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall7>(taken[7]);
      call(this, p, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::setPalette(p);
  }

  //  void QQuickWindowPrivate::clearFocusObject()
  void clearFocusObject() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall8 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::clearFocusObject();
  }

  //  void QQuickWindowPrivate::setFocusToTarget(FocusTarget a0,
  //      Qt::FocusReason a1)
  void setFocusToTarget(
      QWindowPrivate::FocusTarget a0,
      Qt::FocusReason a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall9 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall9>(taken[9]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::setFocusToTarget(a0, a1);
  }

  //  void QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
  //      *event)
  void maybeSynthesizeContextMenuEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall10 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(event);
  }

  //  QWindow *QWindowPrivate::eventReceiver()
  QWindow *eventReceiver() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall11 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QWindowPrivate::eventReceiver();
  }

  //  void QWindowPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall12 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall12>(taken[12]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWindowPrivate::setVisible(visible);
  }

  //  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
  //      const
  QRectF closestAcceptableGeometry(const QRectF &rect) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall13 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall13>(taken[13]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::closestAcceptableGeometry(rect);
  }

  //  bool QWindowPrivate::participatesInLastWindowClosed() const
  bool participatesInLastWindowClosed() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall14 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::participatesInLastWindowClosed();
  }

  //  bool QWindowPrivate::treatAsVisible() const
  bool treatAsVisible() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickApplicationWindowPrivateCall15 call = reinterpret_cast<CuteQQuickApplicationWindowPrivateCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::treatAsVisible();
  }
};

//  QQuickApplicationWindow *QQuickApplicationWindowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickApplicationWindow *ritual_ZN30QQuickApplicationWindowPrivate6q_funcEv(
    QQuickApplicationWindowPrivate *self) {
  return self->q_func();
}

//  const QQuickApplicationWindow *QQuickApplicationWindowPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickApplicationWindow *ritual_ZNK30QQuickApplicationWindowPrivate6q_funcEv(
    const QQuickApplicationWindowPrivate *self) {
  return self->q_func();
}

//  QQuickApplicationWindowPrivate
//      *QQuickApplicationWindowPrivate::get(QQuickApplicationWindow *window)
extern "C" Q_DECL_EXPORT
QQuickApplicationWindowPrivate *ritual_ZN30QQuickApplicationWindowPrivate3getEP23QQuickApplicationWindow(
    QQuickApplicationWindow *window) {
  return QQuickApplicationWindowPrivate::get(window);
}

//  QQmlListProperty<QObject> QQuickApplicationWindowPrivate::contentData()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN30QQuickApplicationWindowPrivate11contentDataEv(
    QQuickApplicationWindowPrivate *self) {
  return new QQmlListProperty<QObject>(self->contentData());
}

//  void QQuickApplicationWindowPrivate::updateHasBackgroundFlags()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate24updateHasBackgroundFlagsEv(
    QQuickApplicationWindowPrivate *self) {
  self->updateHasBackgroundFlags();
}

//  void QQuickApplicationWindowPrivate::relayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate8relayoutEv(
    QQuickApplicationWindowPrivate *self) {
  self->relayout();
}

//  void QQuickApplicationWindowPrivate::itemGeometryChanged(QQuickItem
//      *item, QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void QQuickApplicationWindowPrivate::itemVisibilityChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate21itemVisibilityChangedEP10QQuickItem(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item) {
  self->itemVisibilityChanged(item);
}

//  void QQuickApplicationWindowPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickApplicationWindowPrivate::itemImplicitHeightChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  QPalette QQuickApplicationWindowPrivate::windowPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK30QQuickApplicationWindowPrivate13windowPaletteEv(
    const QQuickApplicationWindowPrivate *self) {
  return new QPalette(self->windowPalette());
}

//  void QQuickApplicationWindowPrivate::updateFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate10updateFontERK5QFont(
    QQuickApplicationWindowPrivate *self,
    const QFont *f) {
  self->updateFont(*f);
}

//  void QQuickApplicationWindowPrivate::setFont_helper(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate14setFont_helperERK5QFont(
    QQuickApplicationWindowPrivate *self,
    const QFont *f) {
  self->setFont_helper(*f);
}

//  void QQuickApplicationWindowPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate11resolveFontEv(
    QQuickApplicationWindowPrivate *self) {
  self->resolveFont();
}

//  void QQuickApplicationWindowPrivate::_q_updateActiveFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate20_q_updateActiveFocusEv(
    QQuickApplicationWindowPrivate *self) {
  self->_q_updateActiveFocus();
}

//  void QQuickApplicationWindowPrivate::setActiveFocusControl(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate21setActiveFocusControlEP10QQuickItem(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item) {
  self->setActiveFocusControl(item);
}

//  void QQuickApplicationWindowPrivate::contentData_append(QQmlListProperty<
//      QObject> *prop, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate18contentData_appendEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *prop,
    QObject *obj) {
  QQuickApplicationWindowPrivate::contentData_append(prop, obj);
}

//  void QQuickApplicationWindowPrivate::cancelBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate16cancelBackgroundEv(
    QQuickApplicationWindowPrivate *self) {
  self->cancelBackground();
}

//  void QQuickApplicationWindowPrivate::executeBackground(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate17executeBackgroundEb(
    QQuickApplicationWindowPrivate *self,
    bool complete) {
  self->executeBackground(complete);
}

//  QPalette QQuickApplicationWindowPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK30QQuickApplicationWindowPrivate14defaultPaletteEv(
    const QQuickApplicationWindowPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  void QQuickApplicationWindowPrivate::updateChildrenPalettes(const
//      QPalette &parentPalette)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickApplicationWindowPrivate22updateChildrenPalettesERK8QPalette(
    QQuickApplicationWindowPrivate *self,
    const QPalette *parentPalette) {
  self->updateChildrenPalettes(*parentPalette);
}

//  a Python function taken by a CuteQQuickApplicationWindowPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickApplicationWindowPrivate(
    QQuickApplicationWindowPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickApplicationWindowPrivate *>(self)->take(key, call);
}

//  void QQuickApplicationWindowPrivate::itemGeometryChanged(QQuickItem
//      *item, QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickApplicationWindowPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickApplicationWindowPrivate::itemGeometryChanged(
      item,
      *change,
      *diff);
}

//  void QQuickApplicationWindowPrivate::itemVisibilityChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickApplicationWindowPrivate21itemVisibilityChangedEP10QQuickItem(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item) {
  self->QQuickApplicationWindowPrivate::itemVisibilityChanged(item);
}

//  void QQuickApplicationWindowPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickApplicationWindowPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item) {
  self->QQuickApplicationWindowPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickApplicationWindowPrivate::itemImplicitHeightChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickApplicationWindowPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickApplicationWindowPrivate *self,
    QQuickItem *item) {
  self->QQuickApplicationWindowPrivate::itemImplicitHeightChanged(item);
}

//  QPalette QQuickApplicationWindowPrivate::windowPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK30QQuickApplicationWindowPrivate13windowPaletteEv(
    const QQuickApplicationWindowPrivate *self) {
  return new QPalette(self->QQuickApplicationWindowPrivate::windowPalette());
}

//  QPalette QQuickApplicationWindowPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK30QQuickApplicationWindowPrivate14defaultPaletteEv(
    const QQuickApplicationWindowPrivate *self) {
  return new QPalette(
      self->QQuickApplicationWindowPrivate::defaultPalette());
}

//  void QQuickApplicationWindowPrivate::updateChildrenPalettes(const
//      QPalette &parentPalette)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickApplicationWindowPrivate22updateChildrenPalettesERK8QPalette(
    QQuickApplicationWindowPrivate *self,
    const QPalette *parentPalette) {
  self->QQuickApplicationWindowPrivate::updateChildrenPalettes(
      *parentPalette);
}

//  a QQmlListProperty<QObject> a ritual of QQuickApplicationWindowPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickApplicationWindowPrivate__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
