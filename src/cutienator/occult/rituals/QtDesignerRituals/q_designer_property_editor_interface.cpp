//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractpropertyeditor.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtDesigner/abstractpropertyeditor.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerPropertyEditorInterface that Python can take functions over in. Every QDesignerPropertyEditorInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerPropertyEditorInterfaceCall0)(const void *, int *);
typedef bool (*CuteQDesignerPropertyEditorInterfaceCall1)(const void *, int *);
typedef void * (*CuteQDesignerPropertyEditorInterfaceCall2)(const void *, int *);
typedef QString * (*CuteQDesignerPropertyEditorInterfaceCall3)(const void *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall4)(const void *, QObject *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall5)(const void *, const QString *, const QVariant *, bool, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall6)(const void *, bool, int *);
typedef int (*CuteQDesignerPropertyEditorInterfaceCall7)(const void *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall8)(const void *, bool, int *);
typedef const QSize * (*CuteQDesignerPropertyEditorInterfaceCall9)(const void *, int *);
typedef const QSize * (*CuteQDesignerPropertyEditorInterfaceCall10)(const void *, int *);
typedef int (*CuteQDesignerPropertyEditorInterfaceCall11)(const void *, int, int *);
typedef bool (*CuteQDesignerPropertyEditorInterfaceCall12)(const void *, int *);
typedef void * (*CuteQDesignerPropertyEditorInterfaceCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerPropertyEditorInterfaceCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall18)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall19)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall25)(const void *, QEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall26)(const void *, QPaintEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall27)(const void *, QMoveEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall28)(const void *, QResizeEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall29)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall30)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall31)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall32)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall33)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall34)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall35)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall36)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall37)(const void *, QShowEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall38)(const void *, QHideEvent *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall39)(const void *, QEvent *, int *);
typedef int (*CuteQDesignerPropertyEditorInterfaceCall40)(const void *, int, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall41)(const void *, QPainter *, int *);
typedef void * (*CuteQDesignerPropertyEditorInterfaceCall42)(const void *, QPoint *, int *);
typedef void * (*CuteQDesignerPropertyEditorInterfaceCall43)(const void *, int *);
typedef void (*CuteQDesignerPropertyEditorInterfaceCall44)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteQDesignerPropertyEditorInterfaceCall45)(const void *, int, int *);
typedef bool (*CuteQDesignerPropertyEditorInterfaceCall46)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerPropertyEditorInterfaceCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerPropertyEditorInterfaceCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerPropertyEditorInterface : public QDesignerPropertyEditorInterface {
public:
  using QDesignerPropertyEditorInterface::QDesignerPropertyEditorInterface;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK32QDesignerPropertyEditorInterface4coreEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerPropertyEditorInterface10isReadOnlyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerPropertyEditorInterface6objectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK32QDesignerPropertyEditorInterface19currentPropertyNameEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerPropertyEditorInterface9setObjectEP7QObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerPropertyEditorInterface16setPropertyValueERK7QStringRK8QVariantb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN32QDesignerPropertyEditorInterface11setReadOnlyEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[29] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[46] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QDesignerFormEditorInterface
  //      *QDesignerPropertyEditorInterface::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall0 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return QDesignerPropertyEditorInterface::core();
  }

  //  bool QDesignerPropertyEditorInterface::isReadOnly() const
  bool isReadOnly() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall1 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QObject *QDesignerPropertyEditorInterface::object() const
  QObject *object() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall2 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }

  //  QString QDesignerPropertyEditorInterface::currentPropertyName() const
  QString currentPropertyName() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall3 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall3>(taken[3]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerPropertyEditorInterface::setObject(QObject *object)
  void setObject(QObject *object) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall4 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall4>(taken[4]);
      call(this, object, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerPropertyEditorInterface::setPropertyValue(const QString
  //      &name, const QVariant &value, bool changed)
  void setPropertyValue(
      const QString &name,
      const QVariant &value,
      bool changed) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall5 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall5>(taken[5]);
      call(this, &name, &value, changed, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerPropertyEditorInterface::setReadOnly(bool readOnly)
  void setReadOnly(bool readOnly) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall6 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall6>(taken[6]);
      call(this, readOnly, &handled);
      if (handled) return;
    }
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall7 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall8 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall9 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall10 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall10>(taken[10]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall11 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall11>(taken[11]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall12 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall13 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidget::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall14 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QWidget::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall15 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mousePressEvent(event);
  }

  //  void QWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall16 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseReleaseEvent(event);
  }

  //  void QWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall17 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseDoubleClickEvent(event);
  }

  //  void QWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall18 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::mouseMoveEvent(event);
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall19 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall20 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall21 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall22 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall23 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall24 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall25 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall26 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::paintEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall27 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall28 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::resizeEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall29 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall30 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall31 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall32 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall33 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall34 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall35 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall36 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall37 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall38 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall39 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall40 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall40>(taken[40]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall41 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall41>(taken[41]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall42 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall42>(taken[42]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall43 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall43>(taken[43]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall44 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall45 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall45>(taken[45]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[46]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall46 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall46>(taken[46]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall47 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall47>(taken[47]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall48 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall49 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall50 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall51 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQDesignerPropertyEditorInterfaceCall52 call = reinterpret_cast<CuteQDesignerPropertyEditorInterfaceCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerPropertyEditorInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QDesignerPropertyEditorInterface10metaObjectEv(
    const QDesignerPropertyEditorInterface *self) {
  return self->metaObject();
}

//  void *QDesignerPropertyEditorInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QDesignerPropertyEditorInterface11qt_metacastEPKc(
    QDesignerPropertyEditorInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDesignerPropertyEditorInterface::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QDesignerPropertyEditorInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDesignerPropertyEditorInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDesignerPropertyEditorInterface::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QDesignerPropertyEditorInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerPropertyEditorInterface::tr(s, c, n));
}

//  QDesignerPropertyEditorInterface::QDesignerPropertyEditorInterface(QWidge
//      t *parent, Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
QDesignerPropertyEditorInterface *ritual_ZN32QDesignerPropertyEditorInterfaceC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int flags) {
  return new CuteQDesignerPropertyEditorInterface(
      parent,
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  QDesignerPropertyEditorInterface::~QDesignerPropertyEditorInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerPropertyEditorInterfaceD1Ev(
    QDesignerPropertyEditorInterface *self) {
  delete self;
}

//  QDesignerFormEditorInterface *QDesignerPropertyEditorInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK32QDesignerPropertyEditorInterface4coreEv(
    const QDesignerPropertyEditorInterface *self) {
  return self->core();
}

//  bool QDesignerPropertyEditorInterface::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QDesignerPropertyEditorInterface10isReadOnlyEv(
    const QDesignerPropertyEditorInterface *self) {
  return self->isReadOnly();
}

//  QObject *QDesignerPropertyEditorInterface::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK32QDesignerPropertyEditorInterface6objectEv(
    const QDesignerPropertyEditorInterface *self) {
  return self->object();
}

//  QString QDesignerPropertyEditorInterface::currentPropertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QDesignerPropertyEditorInterface19currentPropertyNameEv(
    const QDesignerPropertyEditorInterface *self) {
  return new QString(self->currentPropertyName());
}

//  void QDesignerPropertyEditorInterface::propertyChanged(const QString
//      &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerPropertyEditorInterface15propertyChangedERK7QStringRK8QVariant(
    QDesignerPropertyEditorInterface *self,
    const QString *name,
    const QVariant *value) {
  self->propertyChanged(*name, *value);
}

//  void QDesignerPropertyEditorInterface::setObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerPropertyEditorInterface9setObjectEP7QObject(
    QDesignerPropertyEditorInterface *self,
    QObject *object) {
  self->setObject(object);
}

//  void QDesignerPropertyEditorInterface::setPropertyValue(const QString
//      &name, const QVariant &value, bool changed)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerPropertyEditorInterface16setPropertyValueERK7QStringRK8QVariantb(
    QDesignerPropertyEditorInterface *self,
    const QString *name,
    const QVariant *value,
    bool changed) {
  self->setPropertyValue(*name, *value, changed);
}

//  void QDesignerPropertyEditorInterface::setReadOnly(bool readOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QDesignerPropertyEditorInterface11setReadOnlyEb(
    QDesignerPropertyEditorInterface *self,
    bool readOnly) {
  self->setReadOnly(readOnly);
}

//  a Python function taken by a CuteQDesignerPropertyEditorInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerPropertyEditorInterface(
    QDesignerPropertyEditorInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerPropertyEditorInterface *>(self)->take(key, call);
}

//  QDesignerFormEditorInterface *QDesignerPropertyEditorInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_own_ZNK32QDesignerPropertyEditorInterface4coreEv(
    const QDesignerPropertyEditorInterface *self) {
  return self->QDesignerPropertyEditorInterface::core();
}
