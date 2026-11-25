//  Written by hand on 2026-11-25 from
//  QtAxContainer/qaxwidget.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again. ActiveQt is built for Windows alone, as a
//  static library, so every function of it is compiled into ours.
//  'IUnknown', a COM interface of Windows, and 'QAxAggregated', a class of
//  QtAxServer its header only names, are passed as addresses; a 'ulong' as
//  the number Windows has. Not written: 'qt_metacall', 'qt_static_metacall'
//  and 'qt_metacast', which the meta-object system calls itself; the friends
//  'operator>>' and 'operator<<', which take a 'QDataStream &'; and the
//  templates of 'qobject_cast'. Its Cute class takes no 'propertyWritable'
//  or 'setPropertyWritable' over: they take a 'const char *', which is
//  handed to no Python function.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxContainer/qaxwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAxWidget may call these functions of it. This one
//  is, and makes them free for the rituals to call.
struct OwnQAxWidget : QAxWidget {
  using QAxWidget::initialize;
  using QAxWidget::createHostWindow;
  using QAxWidget::changeEvent;
  using QAxWidget::resizeEvent;
  using QAxWidget::translateKeyEvent;
  using QAxWidget::connectNotify;
};

//  A QAxWidget that Python can take functions over in. Every QAxWidget
//  Python makes is one. Each function below asks the Python function handed
//  over for it, and runs Qt's own without one.
typedef ulong (*CuteQAxWidgetCall0)(const void *, int *);
typedef void (*CuteQAxWidgetCall1)(const void *, ulong, int *);
typedef QString * (*CuteQAxWidgetCall2)(const void *, int *);
typedef bool (*CuteQAxWidgetCall3)(const void *, const QString *, int *);
typedef void (*CuteQAxWidgetCall4)(const void *, int *);
typedef const QSize * (*CuteQAxWidgetCall5)(const void *, int *);
typedef const QSize * (*CuteQAxWidgetCall6)(const void *, int *);
typedef void * (*CuteQAxWidgetCall7)(const void *, int *);
typedef bool (*CuteQAxWidgetCall8)(const void *, IUnknown **, int *);
typedef bool (*CuteQAxWidgetCall9)(const void *, bool, int *);
typedef void (*CuteQAxWidgetCall10)(const void *, QEvent *, int *);
typedef void (*CuteQAxWidgetCall11)(const void *, QResizeEvent *, int *);
typedef bool (*CuteQAxWidgetCall12)(const void *, int, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxWidgetCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQAxWidgetCall14)(const void *, int *);
typedef void (*CuteQAxWidgetCall15)(const void *, bool, int *);
typedef int (*CuteQAxWidgetCall16)(const void *, int, int *);
typedef bool (*CuteQAxWidgetCall17)(const void *, int *);
typedef void * (*CuteQAxWidgetCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxWidgetCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQAxWidgetCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAxWidgetCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAxWidgetCall22)(const void *, QMouseEvent *, int *);
typedef void (*CuteQAxWidgetCall23)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQAxWidgetCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQAxWidgetCall25)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAxWidgetCall26)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAxWidgetCall27)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAxWidgetCall28)(const void *, QFocusEvent *, int *);
typedef void (*CuteQAxWidgetCall29)(const void *, QEnterEvent *, int *);
typedef void (*CuteQAxWidgetCall30)(const void *, QEvent *, int *);
typedef void (*CuteQAxWidgetCall31)(const void *, QPaintEvent *, int *);
typedef void (*CuteQAxWidgetCall32)(const void *, QMoveEvent *, int *);
typedef void (*CuteQAxWidgetCall33)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQAxWidgetCall34)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQAxWidgetCall35)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQAxWidgetCall36)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAxWidgetCall37)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQAxWidgetCall38)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQAxWidgetCall39)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQAxWidgetCall40)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQAxWidgetCall41)(const void *, QShowEvent *, int *);
typedef void (*CuteQAxWidgetCall42)(const void *, QHideEvent *, int *);
typedef int (*CuteQAxWidgetCall43)(const void *, int, int *);
typedef void (*CuteQAxWidgetCall44)(const void *, QPainter *, int *);
typedef void * (*CuteQAxWidgetCall45)(const void *, QPoint *, int *);
typedef void * (*CuteQAxWidgetCall46)(const void *, int *);
typedef void (*CuteQAxWidgetCall47)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQAxWidgetCall48)(const void *, int, int *);
typedef bool (*CuteQAxWidgetCall49)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAxWidgetCall50)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAxWidgetCall51)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAxWidgetCall52)(const void *, QChildEvent *, int *);
typedef void (*CuteQAxWidgetCall53)(const void *, QEvent *, int *);
typedef void (*CuteQAxWidgetCall54)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAxWidget : public QAxWidget {
public:
  using QAxWidget::QAxWidget;
  void *taken[55] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QAxObjectInterface12classContextEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface15setClassContextEm")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAxObjectInterface7controlEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface10setControlERK7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAxObjectInterface12resetControlEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QAxWidget15createAggregateEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QAxBase10initializeEPP8IUnknown")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QAxWidget16createHostWindowEb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QAxWidget17translateKeyEventEii")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[33] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[49] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  ulong QAxWidget::classContext() const
  ulong classContext() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxWidgetCall0 call = reinterpret_cast<CuteQAxWidgetCall0>(taken[0]);
      ulong given = call(this, &handled);
      if (handled) return given;
    }
    return QAxWidget::classContext();
  }

  //  void QAxWidget::setClassContext(ulong classContext)
  void setClassContext(ulong classContext) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAxWidgetCall1 call = reinterpret_cast<CuteQAxWidgetCall1>(taken[1]);
      call(this, classContext, &handled);
      if (handled) return;
    }
    QAxWidget::setClassContext(classContext);
  }

  //  QString QAxWidget::control() const
  QString control() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAxWidgetCall2 call = reinterpret_cast<CuteQAxWidgetCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAxWidget::control();
  }

  //  bool QAxWidget::setControl(const QString &a0)
  bool setControl(const QString &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAxWidgetCall3 call = reinterpret_cast<CuteQAxWidgetCall3>(taken[3]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QAxWidget::setControl(a0);
  }

  //  void QAxWidget::resetControl()
  void resetControl() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAxWidgetCall4 call = reinterpret_cast<CuteQAxWidgetCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAxWidget::resetControl();
  }

  //  QSize QAxWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAxWidgetCall5 call = reinterpret_cast<CuteQAxWidgetCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAxWidget::sizeHint();
  }

  //  QSize QAxWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAxWidgetCall6 call = reinterpret_cast<CuteQAxWidgetCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAxWidget::minimumSizeHint();
  }

  //  QAxAggregated *QAxWidget::createAggregate()
  QAxAggregated *createAggregate() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAxWidgetCall7 call = reinterpret_cast<CuteQAxWidgetCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAxAggregated *>(given);
    }
    return QAxWidget::createAggregate();
  }

  //  bool QAxWidget::initialize(IUnknown **a0)
  bool initialize(IUnknown **a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAxWidgetCall8 call = reinterpret_cast<CuteQAxWidgetCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAxWidget::initialize(a0);
  }

  //  bool QAxWidget::createHostWindow(bool a0)
  bool createHostWindow(bool a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAxWidgetCall9 call = reinterpret_cast<CuteQAxWidgetCall9>(taken[9]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAxWidget::createHostWindow(a0);
  }

  //  void QAxWidget::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAxWidgetCall10 call = reinterpret_cast<CuteQAxWidgetCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAxWidget::changeEvent(e);
  }

  //  void QAxWidget::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAxWidgetCall11 call = reinterpret_cast<CuteQAxWidgetCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAxWidget::resizeEvent(a0);
  }

  //  bool QAxWidget::translateKeyEvent(int message, int keycode) const
  bool translateKeyEvent(int message, int keycode) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAxWidgetCall12 call = reinterpret_cast<CuteQAxWidgetCall12>(taken[12]);
      bool given = call(this, message, keycode, &handled);
      if (handled) return given;
    }
    return QAxWidget::translateKeyEvent(message, keycode);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QAxWidget::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAxWidgetCall13 call = reinterpret_cast<CuteQAxWidgetCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QAxWidget::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAxWidgetCall14 call = reinterpret_cast<CuteQAxWidgetCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAxWidgetCall15 call = reinterpret_cast<CuteQAxWidgetCall15>(taken[15]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAxWidgetCall16 call = reinterpret_cast<CuteQAxWidgetCall16>(taken[16]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAxWidgetCall17 call = reinterpret_cast<CuteQAxWidgetCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAxWidgetCall18 call = reinterpret_cast<CuteQAxWidgetCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAxWidgetCall19 call = reinterpret_cast<CuteQAxWidgetCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAxWidgetCall20 call = reinterpret_cast<CuteQAxWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAxWidgetCall21 call = reinterpret_cast<CuteQAxWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAxWidgetCall22 call = reinterpret_cast<CuteQAxWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAxWidgetCall23 call = reinterpret_cast<CuteQAxWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAxWidgetCall24 call = reinterpret_cast<CuteQAxWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAxWidgetCall25 call = reinterpret_cast<CuteQAxWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAxWidgetCall26 call = reinterpret_cast<CuteQAxWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAxWidgetCall27 call = reinterpret_cast<CuteQAxWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAxWidgetCall28 call = reinterpret_cast<CuteQAxWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAxWidgetCall29 call = reinterpret_cast<CuteQAxWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAxWidgetCall30 call = reinterpret_cast<CuteQAxWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAxWidgetCall31 call = reinterpret_cast<CuteQAxWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAxWidgetCall32 call = reinterpret_cast<CuteQAxWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAxWidgetCall33 call = reinterpret_cast<CuteQAxWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQAxWidgetCall34 call = reinterpret_cast<CuteQAxWidgetCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAxWidgetCall35 call = reinterpret_cast<CuteQAxWidgetCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQAxWidgetCall36 call = reinterpret_cast<CuteQAxWidgetCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAxWidgetCall37 call = reinterpret_cast<CuteQAxWidgetCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }

  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAxWidgetCall38 call = reinterpret_cast<CuteQAxWidgetCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }

  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQAxWidgetCall39 call = reinterpret_cast<CuteQAxWidgetCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }

  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQAxWidgetCall40 call = reinterpret_cast<CuteQAxWidgetCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQAxWidgetCall41 call = reinterpret_cast<CuteQAxWidgetCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQAxWidgetCall42 call = reinterpret_cast<CuteQAxWidgetCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQAxWidgetCall43 call = reinterpret_cast<CuteQAxWidgetCall43>(taken[43]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQAxWidgetCall44 call = reinterpret_cast<CuteQAxWidgetCall44>(taken[44]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQAxWidgetCall45 call = reinterpret_cast<CuteQAxWidgetCall45>(taken[45]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[46]) {
      int handled = 0;
      CuteQAxWidgetCall46 call = reinterpret_cast<CuteQAxWidgetCall46>(taken[46]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQAxWidgetCall47 call = reinterpret_cast<CuteQAxWidgetCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[48]) {
      int handled = 0;
      CuteQAxWidgetCall48 call = reinterpret_cast<CuteQAxWidgetCall48>(taken[48]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[49]) {
      int handled = 0;
      CuteQAxWidgetCall49 call = reinterpret_cast<CuteQAxWidgetCall49>(taken[49]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQAxWidgetCall50 call = reinterpret_cast<CuteQAxWidgetCall50>(taken[50]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQAxWidgetCall51 call = reinterpret_cast<CuteQAxWidgetCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQAxWidgetCall52 call = reinterpret_cast<CuteQAxWidgetCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQAxWidgetCall53 call = reinterpret_cast<CuteQAxWidgetCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[54]) {
      int handled = 0;
      CuteQAxWidgetCall54 call = reinterpret_cast<CuteQAxWidgetCall54>(taken[54]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QAxWidget::QAxWidget(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QAxWidget *ritual_ZN9QAxWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new CuteQAxWidget(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QAxWidget::QAxWidget(const QString &c, QWidget *parent, Qt::WindowFlags
//      f)
extern "C" Q_DECL_EXPORT
QAxWidget *ritual_ZN9QAxWidgetC1ERK7QStringP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    const QString *c,
    QWidget *parent,
    int f) {
  return new CuteQAxWidget(*c, parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QAxWidget::QAxWidget(IUnknown *iface, QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QAxWidget *ritual_ZN9QAxWidgetC1EP8IUnknownP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    IUnknown *iface,
    QWidget *parent,
    int f) {
  return new CuteQAxWidget(
      iface,
      parent,
      QFlags<Qt::WindowType>::fromInt(f));
}

//  QAxWidget::~QAxWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxWidgetD1Ev(QAxWidget *self) {
  delete self;
}

//  ulong QAxWidget::classContext() const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK9QAxWidget12classContextEv(const QAxWidget *self) {
  return self->classContext();
}

//  void QAxWidget::setClassContext(ulong classContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxWidget15setClassContextEm(
    QAxWidget *self,
    ulong classContext) {
  self->setClassContext(classContext);
}

//  QString QAxWidget::control() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QAxWidget7controlEv(const QAxWidget *self) {
  return new QString(self->control());
}

//  bool QAxWidget::setControl(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QAxWidget10setControlERK7QString(
    QAxWidget *self,
    const QString *a0) {
  return self->setControl(*a0);
}

//  void QAxWidget::resetControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxWidget12resetControlEv(QAxWidget *self) {
  self->resetControl();
}

//  void QAxWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxWidget5clearEv(QAxWidget *self) {
  self->clear();
}

//  bool QAxWidget::doVerb(const QString &verb)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QAxWidget6doVerbERK7QString(
    QAxWidget *self,
    const QString *verb) {
  return self->doVerb(*verb);
}

//  QSize QAxWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QAxWidget8sizeHintEv(const QAxWidget *self) {
  return new QSize(self->sizeHint());
}

//  QSize QAxWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QAxWidget15minimumSizeHintEv(const QAxWidget *self) {
  return new QSize(self->minimumSizeHint());
}

//  QAxAggregated *QAxWidget::createAggregate()
extern "C" Q_DECL_EXPORT
QAxAggregated *ritual_ZN9QAxWidget15createAggregateEv(QAxWidget *self) {
  return self->createAggregate();
}

//  const QMetaObject *QAxWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QAxWidget10metaObjectEv(
    const QAxWidget *self) {
  return self->metaObject();
}

//  bool QAxWidget::initialize(IUnknown **a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QAxWidget10initializeEPP8IUnknown(
    QAxWidget *self,
    IUnknown **a0) {
  return self->initialize(a0);
}

//  bool QAxWidget::createHostWindow(bool a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QAxWidget16createHostWindowEb(QAxWidget *self, bool a0) {
  return self->createHostWindow(a0);
}

//  bool QAxWidget::createHostWindow(bool a0, const QByteArray &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QAxWidget16createHostWindowEbRK10QByteArray(
    QAxWidget *self,
    bool a0,
    const QByteArray *a1) {
  return self->createHostWindow(a0, *a1);
}

//  void QAxWidget::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxWidget11changeEventEP6QEvent(QAxWidget *self, QEvent *e) {
  self->changeEvent(e);
}

//  void QAxWidget::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxWidget11resizeEventEP12QResizeEvent(
    QAxWidget *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  bool QAxWidget::translateKeyEvent(int message, int keycode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QAxWidget17translateKeyEventEii(
    const QAxWidget *self,
    int message,
    int keycode) {
  return self->translateKeyEvent(message, keycode);
}

//  void QAxWidget::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QAxWidget13connectNotifyERK11QMetaMethod(
    QAxWidget *self,
    const QMetaMethod *signal) {
  self->connectNotify(*signal);
}

//  QAxWidgetPrivate *QAxWidget::d_func()
extern "C" Q_DECL_EXPORT
QAxWidgetPrivate *ritual_ZN9QAxWidget6d_funcEv(QAxWidget *self) {
  return self->d_func();
}

//  const QAxWidgetPrivate *QAxWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QAxWidgetPrivate *ritual_ZNK9QAxWidget6d_funcEv(
    const QAxWidget *self) {
  return self->d_func();
}

//  QAxWidget as the QAxBase it is built on
extern "C" Q_DECL_EXPORT
QAxBase *ritual_cast_QAxWidget_QAxBase(QAxWidget *self) {
  return static_cast<QAxBase *>(self);
}

//  a Python function taken by a CuteQAxWidget, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxWidget(QAxWidget *self, const char *key, void *call) {
  return static_cast<CuteQAxWidget *>(self)->take(key, call);
}

//  ulong QAxWidget::classContext() const
extern "C" Q_DECL_EXPORT
ulong ritual_own_ZNK9QAxWidget12classContextEv(const QAxWidget *self) {
  return self->QAxWidget::classContext();
}

//  void QAxWidget::setClassContext(ulong classContext)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QAxWidget15setClassContextEm(
    QAxWidget *self,
    ulong classContext) {
  self->QAxWidget::setClassContext(classContext);
}

//  QString QAxWidget::control() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK9QAxWidget7controlEv(const QAxWidget *self) {
  return new QString(self->QAxWidget::control());
}

//  bool QAxWidget::setControl(const QString &a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QAxWidget10setControlERK7QString(
    QAxWidget *self,
    const QString *a0) {
  return self->QAxWidget::setControl(*a0);
}

//  void QAxWidget::resetControl()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QAxWidget12resetControlEv(QAxWidget *self) {
  self->QAxWidget::resetControl();
}

//  QSize QAxWidget::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QAxWidget8sizeHintEv(const QAxWidget *self) {
  return new QSize(self->QAxWidget::sizeHint());
}

//  QSize QAxWidget::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QAxWidget15minimumSizeHintEv(const QAxWidget *self) {
  return new QSize(self->QAxWidget::minimumSizeHint());
}

//  QAxAggregated *QAxWidget::createAggregate()
extern "C" Q_DECL_EXPORT
QAxAggregated *ritual_own_ZN9QAxWidget15createAggregateEv(QAxWidget *self) {
  return self->QAxWidget::createAggregate();
}

//  bool QAxWidget::initialize(IUnknown **a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QAxWidget10initializeEPP8IUnknown(
    QAxWidget *self,
    IUnknown **a0) {
  return static_cast<OwnQAxWidget *>(self)->OwnQAxWidget::initialize(a0);
}

//  bool QAxWidget::createHostWindow(bool a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QAxWidget16createHostWindowEb(QAxWidget *self, bool a0) {
  return static_cast<OwnQAxWidget *>(self)->OwnQAxWidget::createHostWindow(
      a0);
}

//  void QAxWidget::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QAxWidget11changeEventEP6QEvent(
    QAxWidget *self,
    QEvent *e) {
  static_cast<OwnQAxWidget *>(self)->OwnQAxWidget::changeEvent(e);
}

//  void QAxWidget::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QAxWidget11resizeEventEP12QResizeEvent(
    QAxWidget *self,
    QResizeEvent *a0) {
  static_cast<OwnQAxWidget *>(self)->OwnQAxWidget::resizeEvent(a0);
}

//  bool QAxWidget::translateKeyEvent(int message, int keycode) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QAxWidget17translateKeyEventEii(
    const QAxWidget *self,
    int message,
    int keycode) {
  return static_cast<const OwnQAxWidget *>(self)->OwnQAxWidget::translateKeyEvent(
      message,
      keycode);
}

//  void QAxWidget::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QAxWidget13connectNotifyERK11QMetaMethod(
    QAxWidget *self,
    const QMetaMethod *signal) {
  static_cast<OwnQAxWidget *>(self)->OwnQAxWidget::connectNotify(*signal);
}

#endif  // defined(Q_OS_WIN)
