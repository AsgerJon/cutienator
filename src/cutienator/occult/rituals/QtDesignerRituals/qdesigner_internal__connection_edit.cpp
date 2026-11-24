//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on qdesigner_internal::ConnectionEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_ConnectionEdit : qdesigner_internal::ConnectionEdit {
  using qdesigner_internal::ConnectionEdit::paintEvent;
  using qdesigner_internal::ConnectionEdit::mouseMoveEvent;
  using qdesigner_internal::ConnectionEdit::mousePressEvent;
  using qdesigner_internal::ConnectionEdit::mouseReleaseEvent;
  using qdesigner_internal::ConnectionEdit::keyPressEvent;
  using qdesigner_internal::ConnectionEdit::mouseDoubleClickEvent;
  using qdesigner_internal::ConnectionEdit::resizeEvent;
  using qdesigner_internal::ConnectionEdit::contextMenuEvent;
  using qdesigner_internal::ConnectionEdit::createConnection;
  using qdesigner_internal::ConnectionEdit::modifyConnection;
  using qdesigner_internal::ConnectionEdit::widgetAt;
  using qdesigner_internal::ConnectionEdit::endConnection;
};

//  A qdesigner_internal::ConnectionEdit that Python can take functions over in. Every qdesigner_internal::ConnectionEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cuteqdesigner_internal_ConnectionEditCall0)(const void *, qdesigner_internal::Connection *, const QString *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall1)(const void *, qdesigner_internal::Connection *, const QString *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall2)(const void *, QShowEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall3)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall4)(const void *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall5)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall6)(const void *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall7)(const void *, QObject *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall8)(const void *, QPaintEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall9)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall10)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall11)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall12)(const void *, QKeyEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall13)(const void *, QMouseEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall14)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall15)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void * (*Cuteqdesigner_internal_ConnectionEditCall16)(const void *, QWidget *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall17)(const void *, qdesigner_internal::Connection *, int *);
typedef void * (*Cuteqdesigner_internal_ConnectionEditCall18)(const void *, const QPoint *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall19)(const void *, QWidget *, const QPoint *, int *);
typedef int (*Cuteqdesigner_internal_ConnectionEditCall20)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall21)(const void *, bool, int *);
typedef const QSize * (*Cuteqdesigner_internal_ConnectionEditCall22)(const void *, int *);
typedef const QSize * (*Cuteqdesigner_internal_ConnectionEditCall23)(const void *, int *);
typedef int (*Cuteqdesigner_internal_ConnectionEditCall24)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_ConnectionEditCall25)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_ConnectionEditCall26)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_ConnectionEditCall27)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall28)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall29)(const void *, QKeyEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall30)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall31)(const void *, QFocusEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall32)(const void *, QEnterEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall33)(const void *, QEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall34)(const void *, QMoveEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall35)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall36)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall37)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall38)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall39)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall40)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall41)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall42)(const void *, QHideEvent *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall43)(const void *, QEvent *, int *);
typedef int (*Cuteqdesigner_internal_ConnectionEditCall44)(const void *, int, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall45)(const void *, QPainter *, int *);
typedef void * (*Cuteqdesigner_internal_ConnectionEditCall46)(const void *, QPoint *, int *);
typedef void * (*Cuteqdesigner_internal_ConnectionEditCall47)(const void *, int *);
typedef void (*Cuteqdesigner_internal_ConnectionEditCall48)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*Cuteqdesigner_internal_ConnectionEditCall49)(const void *, int, int *);
typedef bool (*Cuteqdesigner_internal_ConnectionEditCall50)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_ConnectionEditCall51)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall52)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall53)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall54)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall55)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_ConnectionEditCall56)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class Cuteqdesigner_internal_ConnectionEdit : public qdesigner_internal::ConnectionEdit {
public:
  using qdesigner_internal::ConnectionEdit::ConnectionEdit;
  void *taken[57] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit9setSourceEPNS_10ConnectionERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit9setTargetEPNS_10ConnectionERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit14deleteSelectedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit13setBackgroundEP7QWidget")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit16updateBackgroundEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit13widgetRemovedEP7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit13objectRemovedEP7QObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[14] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit16createConnectionEP7QWidgetS2_")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit16modifyConnectionEPNS_10ConnectionE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal14ConnectionEdit8widgetAtERK6QPoint")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal14ConnectionEdit13endConnectionEP7QWidgetRK6QPoint")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[26] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[35] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[50] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[55] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[56] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void qdesigner_internal::ConnectionEdit::setSource(Connection *con,
  //      const QString &obj_name)
  void setSource(
      qdesigner_internal::Connection *con,
      const QString &obj_name) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall0 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall0>(taken[0]);
      call(this, con, &obj_name, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::setSource(con, obj_name);
  }

  //  void qdesigner_internal::ConnectionEdit::setTarget(Connection *con,
  //      const QString &obj_name)
  void setTarget(
      qdesigner_internal::Connection *con,
      const QString &obj_name) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall1 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall1>(taken[1]);
      call(this, con, &obj_name, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::setTarget(con, obj_name);
  }

  //  void qdesigner_internal::ConnectionEdit::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall2 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::showEvent(a0);
  }

  //  void qdesigner_internal::ConnectionEdit::deleteSelected()
  void deleteSelected() override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall3 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::deleteSelected();
  }

  //  void qdesigner_internal::ConnectionEdit::setBackground(QWidget
  //      *background)
  void setBackground(QWidget *background) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall4 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall4>(taken[4]);
      call(this, background, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::setBackground(background);
  }

  //  void qdesigner_internal::ConnectionEdit::updateBackground()
  void updateBackground() override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall5 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::updateBackground();
  }

  //  void qdesigner_internal::ConnectionEdit::widgetRemoved(QWidget *w)
  void widgetRemoved(QWidget *w) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall6 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall6>(taken[6]);
      call(this, w, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::widgetRemoved(w);
  }

  //  void qdesigner_internal::ConnectionEdit::objectRemoved(QObject *o)
  void objectRemoved(QObject *o) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall7 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall7>(taken[7]);
      call(this, o, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::objectRemoved(o);
  }

  //  void qdesigner_internal::ConnectionEdit::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall8 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::paintEvent(e);
  }

  //  void qdesigner_internal::ConnectionEdit::mouseMoveEvent(QMouseEvent
  //      *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall9 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::mouseMoveEvent(e);
  }

  //  void qdesigner_internal::ConnectionEdit::mousePressEvent(QMouseEvent
  //      *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall10 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::mousePressEvent(e);
  }

  //  void
  //      qdesigner_internal::ConnectionEdit::mouseReleaseEvent(QMouseEvent
  //      *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall11 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::mouseReleaseEvent(e);
  }

  //  void qdesigner_internal::ConnectionEdit::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall12 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::keyPressEvent(e);
  }

  //  void
  //      qdesigner_internal::ConnectionEdit::mouseDoubleClickEvent(QMouseE
  //      vent *e)
  void mouseDoubleClickEvent(QMouseEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall13 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::mouseDoubleClickEvent(e);
  }

  //  void qdesigner_internal::ConnectionEdit::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall14 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::resizeEvent(e);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void qdesigner_internal::ConnectionEdit::contextMenuEvent(QContextMen
  //      uEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall15 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  Connection
  //      *qdesigner_internal::ConnectionEdit::createConnection(QWidget
  //      *source, QWidget *target)
  qdesigner_internal::Connection *createConnection(
      QWidget *source,
      QWidget *target) override {
    if (taken[16]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall16 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall16>(taken[16]);
      void * given = call(this, source, target, &handled);
      if (handled) return static_cast<qdesigner_internal::Connection *>(given);
    }
    return qdesigner_internal::ConnectionEdit::createConnection(source, target);
  }

  //  void qdesigner_internal::ConnectionEdit::modifyConnection(Connection
  //      *con)
  void modifyConnection(qdesigner_internal::Connection *con) override {
    if (taken[17]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall17 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall17>(taken[17]);
      call(this, con, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::modifyConnection(con);
  }

  //  QWidget *qdesigner_internal::ConnectionEdit::widgetAt(const QPoint
  //      &pos) const
  QWidget *widgetAt(const QPoint &pos) const override {
    if (taken[18]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall18 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall18>(taken[18]);
      void * given = call(this, &pos, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return qdesigner_internal::ConnectionEdit::widgetAt(pos);
  }

  //  void qdesigner_internal::ConnectionEdit::endConnection(QWidget
  //      *target, const QPoint &pos)
  void endConnection(QWidget *target, const QPoint &pos) override {
    if (taken[19]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall19 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall19>(taken[19]);
      call(this, target, &pos, &handled);
      if (handled) return;
    }
    qdesigner_internal::ConnectionEdit::endConnection(target, pos);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[20]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall20 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[21]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall21 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall21>(taken[21]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[22]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall22 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall22>(taken[22]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[23]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall23 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall23>(taken[23]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[24]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall24 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall24>(taken[24]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[25]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall25 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[26]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall26 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall27 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall27>(taken[27]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall28 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall29 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall30 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall31 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall32 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall33 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall34 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall35 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall36 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall37 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall38 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall39 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall40 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall41 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall42 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[43]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall43 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[44]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall44 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall44>(taken[44]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[45]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall45 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall45>(taken[45]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[46]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall46 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall46>(taken[46]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[47]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall47 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall47>(taken[47]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[48]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall48 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall48>(taken[48]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[49]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall49 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall49>(taken[49]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[50]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall50 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall50>(taken[50]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall51 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall51>(taken[51]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall52 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall53 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall54 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[55]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall55 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall55>(taken[55]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[56]) {
      int handled = 0;
      Cuteqdesigner_internal_ConnectionEditCall56 call = reinterpret_cast<Cuteqdesigner_internal_ConnectionEditCall56>(taken[56]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *qdesigner_internal::ConnectionEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14ConnectionEdit10metaObjectEv(
    const qdesigner_internal::ConnectionEdit *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::ConnectionEdit::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14ConnectionEdit2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::ConnectionEdit::tr(s, c, n));
}

//  int qdesigner_internal::ConnectionEdit::connectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14ConnectionEdit15connectionCountEv(
    const qdesigner_internal::ConnectionEdit *self) {
  return self->connectionCount();
}

//  Connection *qdesigner_internal::ConnectionEdit::connection(int i) const
extern "C" Q_DECL_EXPORT
qdesigner_internal::Connection *ritual_ZNK18qdesigner_internal14ConnectionEdit10connectionEi(
    const qdesigner_internal::ConnectionEdit *self,
    int i) {
  return self->connection(i);
}

//  int qdesigner_internal::ConnectionEdit::indexOfConnection(Connection
//      *con) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14ConnectionEdit17indexOfConnectionEPNS_10ConnectionE(
    const qdesigner_internal::ConnectionEdit *self,
    qdesigner_internal::Connection *con) {
  return self->indexOfConnection(con);
}

//  void qdesigner_internal::ConnectionEdit::setSource(Connection *con, const
//      QString &obj_name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit9setSourceEPNS_10ConnectionERK7QString(
    qdesigner_internal::ConnectionEdit *self,
    qdesigner_internal::Connection *con,
    const QString *obj_name) {
  self->setSource(con, *obj_name);
}

//  void qdesigner_internal::ConnectionEdit::setTarget(Connection *con, const
//      QString &obj_name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit9setTargetEPNS_10ConnectionERK7QString(
    qdesigner_internal::ConnectionEdit *self,
    qdesigner_internal::Connection *con,
    const QString *obj_name) {
  self->setTarget(con, *obj_name);
}

//  QUndoStack *qdesigner_internal::ConnectionEdit::undoStack() const
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZNK18qdesigner_internal14ConnectionEdit9undoStackEv(
    const qdesigner_internal::ConnectionEdit *self) {
  return self->undoStack();
}

//  void qdesigner_internal::ConnectionEdit::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit9showEventEP10QShowEvent(
    qdesigner_internal::ConnectionEdit *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void qdesigner_internal::ConnectionEdit::deleteSelected()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit14deleteSelectedEv(
    qdesigner_internal::ConnectionEdit *self) {
  self->deleteSelected();
}

//  void qdesigner_internal::ConnectionEdit::setBackground(QWidget
//      *background)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit13setBackgroundEP7QWidget(
    qdesigner_internal::ConnectionEdit *self,
    QWidget *background) {
  self->setBackground(background);
}

//  void qdesigner_internal::ConnectionEdit::updateBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit16updateBackgroundEv(
    qdesigner_internal::ConnectionEdit *self) {
  self->updateBackground();
}

//  void qdesigner_internal::ConnectionEdit::widgetRemoved(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit13widgetRemovedEP7QWidget(
    qdesigner_internal::ConnectionEdit *self,
    QWidget *w) {
  self->widgetRemoved(w);
}

//  void qdesigner_internal::ConnectionEdit::objectRemoved(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit13objectRemovedEP7QObject(
    qdesigner_internal::ConnectionEdit *self,
    QObject *o) {
  self->objectRemoved(o);
}

//  Connection *qdesigner_internal::ConnectionEdit::createConnection(QWidget
//      *source, QWidget *target)
extern "C" Q_DECL_EXPORT
qdesigner_internal::Connection *ritual_ZN18qdesigner_internal14ConnectionEdit16createConnectionEP7QWidgetS2_(
    qdesigner_internal::ConnectionEdit *self,
    QWidget *source,
    QWidget *target) {
  return self->createConnection(source, target);
}

//  void qdesigner_internal::ConnectionEdit::modifyConnection(Connection
//      *con)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit16modifyConnectionEPNS_10ConnectionE(
    qdesigner_internal::ConnectionEdit *self,
    qdesigner_internal::Connection *con) {
  self->modifyConnection(con);
}

//  QWidget *qdesigner_internal::ConnectionEdit::widgetAt(const QPoint &pos)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal14ConnectionEdit8widgetAtERK6QPoint(
    const qdesigner_internal::ConnectionEdit *self,
    const QPoint *pos) {
  return self->widgetAt(*pos);
}

//  void qdesigner_internal::ConnectionEdit::endConnection(QWidget *target,
//      const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14ConnectionEdit13endConnectionEP7QWidgetRK6QPoint(
    qdesigner_internal::ConnectionEdit *self,
    QWidget *target,
    const QPoint *pos) {
  self->endConnection(target, *pos);
}

//  Connection *qdesigner_internal::ConnectionEdit::newlyAddedConnection()
extern "C" Q_DECL_EXPORT
qdesigner_internal::Connection *ritual_ZN18qdesigner_internal14ConnectionEdit20newlyAddedConnectionEv(
    qdesigner_internal::ConnectionEdit *self) {
  return self->newlyAddedConnection();
}

//  qdesigner_internal::ConnectionEdit as the qdesigner_internal::CETypes it
//      is built on
extern "C" Q_DECL_EXPORT
qdesigner_internal::CETypes *ritual_cast_qdesigner_internal_ConnectionEdit_qdesigner_internal_CETypes(
    qdesigner_internal::ConnectionEdit *self) {
  return static_cast<qdesigner_internal::CETypes *>(self);
}

//  a Python function taken by a Cuteqdesigner_internal_ConnectionEdit, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_ConnectionEdit(
    qdesigner_internal::ConnectionEdit *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_ConnectionEdit *>(self)->take(key, call);
}

//  void qdesigner_internal::ConnectionEdit::setSource(Connection *con, const
//      QString &obj_name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit9setSourceEPNS_10ConnectionERK7QString(
    qdesigner_internal::ConnectionEdit *self,
    qdesigner_internal::Connection *con,
    const QString *obj_name) {
  self->qdesigner_internal::ConnectionEdit::setSource(con, *obj_name);
}

//  void qdesigner_internal::ConnectionEdit::setTarget(Connection *con, const
//      QString &obj_name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit9setTargetEPNS_10ConnectionERK7QString(
    qdesigner_internal::ConnectionEdit *self,
    qdesigner_internal::Connection *con,
    const QString *obj_name) {
  self->qdesigner_internal::ConnectionEdit::setTarget(con, *obj_name);
}

//  void qdesigner_internal::ConnectionEdit::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit9showEventEP10QShowEvent(
    qdesigner_internal::ConnectionEdit *self,
    QShowEvent *a0) {
  self->qdesigner_internal::ConnectionEdit::showEvent(a0);
}

//  void qdesigner_internal::ConnectionEdit::deleteSelected()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit14deleteSelectedEv(
    qdesigner_internal::ConnectionEdit *self) {
  self->qdesigner_internal::ConnectionEdit::deleteSelected();
}

//  void qdesigner_internal::ConnectionEdit::setBackground(QWidget
//      *background)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit13setBackgroundEP7QWidget(
    qdesigner_internal::ConnectionEdit *self,
    QWidget *background) {
  self->qdesigner_internal::ConnectionEdit::setBackground(background);
}

//  void qdesigner_internal::ConnectionEdit::updateBackground()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit16updateBackgroundEv(
    qdesigner_internal::ConnectionEdit *self) {
  self->qdesigner_internal::ConnectionEdit::updateBackground();
}

//  void qdesigner_internal::ConnectionEdit::widgetRemoved(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit13widgetRemovedEP7QWidget(
    qdesigner_internal::ConnectionEdit *self,
    QWidget *w) {
  self->qdesigner_internal::ConnectionEdit::widgetRemoved(w);
}

//  void qdesigner_internal::ConnectionEdit::objectRemoved(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit13objectRemovedEP7QObject(
    qdesigner_internal::ConnectionEdit *self,
    QObject *o) {
  self->qdesigner_internal::ConnectionEdit::objectRemoved(o);
}

//  void qdesigner_internal::ConnectionEdit::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit10paintEventEP11QPaintEvent(
    qdesigner_internal::ConnectionEdit *self,
    QPaintEvent *e) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::paintEvent(
      e);
}

//  void qdesigner_internal::ConnectionEdit::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit14mouseMoveEventEP11QMouseEvent(
    qdesigner_internal::ConnectionEdit *self,
    QMouseEvent *e) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::mouseMoveEvent(
      e);
}

//  void qdesigner_internal::ConnectionEdit::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit15mousePressEventEP11QMouseEvent(
    qdesigner_internal::ConnectionEdit *self,
    QMouseEvent *e) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::mousePressEvent(
      e);
}

//  void qdesigner_internal::ConnectionEdit::mouseReleaseEvent(QMouseEvent
//      *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit17mouseReleaseEventEP11QMouseEvent(
    qdesigner_internal::ConnectionEdit *self,
    QMouseEvent *e) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::mouseReleaseEvent(
      e);
}

//  void qdesigner_internal::ConnectionEdit::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit13keyPressEventEP9QKeyEvent(
    qdesigner_internal::ConnectionEdit *self,
    QKeyEvent *e) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::keyPressEvent(
      e);
}

//  void
//      qdesigner_internal::ConnectionEdit::mouseDoubleClickEvent(QMouseEvent
//      *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit21mouseDoubleClickEventEP11QMouseEvent(
    qdesigner_internal::ConnectionEdit *self,
    QMouseEvent *e) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::mouseDoubleClickEvent(
      e);
}

//  void qdesigner_internal::ConnectionEdit::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit11resizeEventEP12QResizeEvent(
    qdesigner_internal::ConnectionEdit *self,
    QResizeEvent *e) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::resizeEvent(
      e);
}

//  void
//      qdesigner_internal::ConnectionEdit::contextMenuEvent(QContextMenuEven
//      t *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit16contextMenuEventEP17QContextMenuEvent(
    qdesigner_internal::ConnectionEdit *self,
    QContextMenuEvent *event) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::contextMenuEvent(
      event);
}

//  Connection *qdesigner_internal::ConnectionEdit::createConnection(QWidget
//      *source, QWidget *target)
extern "C" Q_DECL_EXPORT
qdesigner_internal::Connection *ritual_own_ZN18qdesigner_internal14ConnectionEdit16createConnectionEP7QWidgetS2_(
    qdesigner_internal::ConnectionEdit *self,
    QWidget *source,
    QWidget *target) {
  return static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::createConnection(
      source,
      target);
}

//  void qdesigner_internal::ConnectionEdit::modifyConnection(Connection
//      *con)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit16modifyConnectionEPNS_10ConnectionE(
    qdesigner_internal::ConnectionEdit *self,
    qdesigner_internal::Connection *con) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::modifyConnection(
      con);
}

//  QWidget *qdesigner_internal::ConnectionEdit::widgetAt(const QPoint &pos)
//      const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18qdesigner_internal14ConnectionEdit8widgetAtERK6QPoint(
    const qdesigner_internal::ConnectionEdit *self,
    const QPoint *pos) {
  return static_cast<const Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::widgetAt(
      *pos);
}

//  void qdesigner_internal::ConnectionEdit::endConnection(QWidget *target,
//      const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal14ConnectionEdit13endConnectionEP7QWidgetRK6QPoint(
    qdesigner_internal::ConnectionEdit *self,
    QWidget *target,
    const QPoint *pos) {
  static_cast<Ownqdesigner_internal_ConnectionEdit *>(self)->Ownqdesigner_internal_ConnectionEdit::endConnection(
      target,
      *pos);
}
