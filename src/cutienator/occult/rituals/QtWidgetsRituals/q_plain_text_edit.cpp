//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qplaintextedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qplaintextedit.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QPlainTextEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPlainTextEdit : QPlainTextEdit {
  using QPlainTextEdit::event;
  using QPlainTextEdit::timerEvent;
  using QPlainTextEdit::keyPressEvent;
  using QPlainTextEdit::keyReleaseEvent;
  using QPlainTextEdit::resizeEvent;
  using QPlainTextEdit::paintEvent;
  using QPlainTextEdit::mousePressEvent;
  using QPlainTextEdit::mouseMoveEvent;
  using QPlainTextEdit::mouseReleaseEvent;
  using QPlainTextEdit::mouseDoubleClickEvent;
  using QPlainTextEdit::focusNextPrevChild;
  using QPlainTextEdit::contextMenuEvent;
  using QPlainTextEdit::dragEnterEvent;
  using QPlainTextEdit::dragLeaveEvent;
  using QPlainTextEdit::dragMoveEvent;
  using QPlainTextEdit::dropEvent;
  using QPlainTextEdit::focusInEvent;
  using QPlainTextEdit::focusOutEvent;
  using QPlainTextEdit::showEvent;
  using QPlainTextEdit::changeEvent;
  using QPlainTextEdit::wheelEvent;
  using QPlainTextEdit::createMimeDataFromSelection;
  using QPlainTextEdit::canInsertFromMimeData;
  using QPlainTextEdit::insertFromMimeData;
  using QPlainTextEdit::inputMethodEvent;
  using QPlainTextEdit::scrollContentsBy;
  using QPlainTextEdit::doSetTextCursor;
};

//  A QPlainTextEdit that Python can take functions over in. Every QPlainTextEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQPlainTextEditCall0)(const void *, int, const QUrl *, int *);
typedef const QVariant * (*CuteQPlainTextEditCall1)(const void *, int, int *);
typedef bool (*CuteQPlainTextEditCall2)(const void *, QEvent *, int *);
typedef void (*CuteQPlainTextEditCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQPlainTextEditCall4)(const void *, QKeyEvent *, int *);
typedef void (*CuteQPlainTextEditCall5)(const void *, QKeyEvent *, int *);
typedef void (*CuteQPlainTextEditCall6)(const void *, QResizeEvent *, int *);
typedef void (*CuteQPlainTextEditCall7)(const void *, QPaintEvent *, int *);
typedef void (*CuteQPlainTextEditCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPlainTextEditCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPlainTextEditCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQPlainTextEditCall11)(const void *, QMouseEvent *, int *);
typedef bool (*CuteQPlainTextEditCall12)(const void *, bool, int *);
typedef void (*CuteQPlainTextEditCall13)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQPlainTextEditCall14)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQPlainTextEditCall15)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQPlainTextEditCall16)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQPlainTextEditCall17)(const void *, QDropEvent *, int *);
typedef void (*CuteQPlainTextEditCall18)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPlainTextEditCall19)(const void *, QFocusEvent *, int *);
typedef void (*CuteQPlainTextEditCall20)(const void *, QShowEvent *, int *);
typedef void (*CuteQPlainTextEditCall21)(const void *, QEvent *, int *);
typedef void (*CuteQPlainTextEditCall22)(const void *, QWheelEvent *, int *);
typedef void * (*CuteQPlainTextEditCall23)(const void *, int *);
typedef bool (*CuteQPlainTextEditCall24)(const void *, const QMimeData *, int *);
typedef void (*CuteQPlainTextEditCall25)(const void *, const QMimeData *, int *);
typedef void (*CuteQPlainTextEditCall26)(const void *, QInputMethodEvent *, int *);
typedef void (*CuteQPlainTextEditCall27)(const void *, int, int, int *);
typedef void (*CuteQPlainTextEditCall28)(const void *, const QTextCursor *, int *);
typedef const QSize * (*CuteQPlainTextEditCall29)(const void *, int *);
typedef const QSize * (*CuteQPlainTextEditCall30)(const void *, int *);
typedef void (*CuteQPlainTextEditCall31)(const void *, QWidget *, int *);
typedef bool (*CuteQPlainTextEditCall32)(const void *, QObject *, QEvent *, int *);
typedef bool (*CuteQPlainTextEditCall33)(const void *, QEvent *, int *);
typedef const QSize * (*CuteQPlainTextEditCall34)(const void *, int *);
typedef void (*CuteQPlainTextEditCall35)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQPlainTextEditCall36)(const void *, int *);
typedef void (*CuteQPlainTextEditCall37)(const void *, bool, int *);
typedef int (*CuteQPlainTextEditCall38)(const void *, int, int *);
typedef bool (*CuteQPlainTextEditCall39)(const void *, int *);
typedef void * (*CuteQPlainTextEditCall40)(const void *, int *);
typedef void (*CuteQPlainTextEditCall41)(const void *, QEnterEvent *, int *);
typedef void (*CuteQPlainTextEditCall42)(const void *, QEvent *, int *);
typedef void (*CuteQPlainTextEditCall43)(const void *, QMoveEvent *, int *);
typedef void (*CuteQPlainTextEditCall44)(const void *, QCloseEvent *, int *);
typedef void (*CuteQPlainTextEditCall45)(const void *, QTabletEvent *, int *);
typedef void (*CuteQPlainTextEditCall46)(const void *, QActionEvent *, int *);
typedef void (*CuteQPlainTextEditCall47)(const void *, QHideEvent *, int *);
typedef int (*CuteQPlainTextEditCall48)(const void *, int, int *);
typedef void (*CuteQPlainTextEditCall49)(const void *, QPainter *, int *);
typedef void * (*CuteQPlainTextEditCall50)(const void *, QPoint *, int *);
typedef void * (*CuteQPlainTextEditCall51)(const void *, int *);
typedef void (*CuteQPlainTextEditCall52)(const void *, QChildEvent *, int *);
typedef void (*CuteQPlainTextEditCall53)(const void *, QEvent *, int *);
typedef void (*CuteQPlainTextEditCall54)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQPlainTextEditCall55)(const void *, const QMetaMethod *, int *);
class CuteQPlainTextEdit : public QPlainTextEdit {
public:
  using QPlainTextEdit::QPlainTextEdit;
  void *taken[56] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QPlainTextEdit12loadResourceEiRK4QUrl")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlainTextEdit27createMimeDataFromSelectionEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QPlainTextEdit21canInsertFromMimeDataEPK9QMimeData")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPlainTextEdit18insertFromMimeDataEPK9QMimeData")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QPlainTextEdit15doSetTextCursorERK11QTextCursor")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
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
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[55] = call;
      return true;
    }
    return false;
  }

  //  QVariant QPlainTextEdit::loadResource(int type, const QUrl &name)
  QVariant loadResource(int type, const QUrl &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlainTextEditCall0 call = reinterpret_cast<CuteQPlainTextEditCall0>(taken[0]);
      const QVariant * given = call(this, type, &name, &handled);
      if (handled && given) return *given;
    }
    return QPlainTextEdit::loadResource(type, name);
  }

  //  QVariant QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery
  //      property) const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlainTextEditCall1 call = reinterpret_cast<CuteQPlainTextEditCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QPlainTextEdit::inputMethodQuery(property);
  }

  //  bool QPlainTextEdit::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlainTextEditCall2 call = reinterpret_cast<CuteQPlainTextEditCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QPlainTextEdit::event(e);
  }

  //  void QPlainTextEdit::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlainTextEditCall3 call = reinterpret_cast<CuteQPlainTextEditCall3>(taken[3]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::timerEvent(e);
  }

  //  void QPlainTextEdit::keyPressEvent(QKeyEvent *e)
  void keyPressEvent(QKeyEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlainTextEditCall4 call = reinterpret_cast<CuteQPlainTextEditCall4>(taken[4]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::keyPressEvent(e);
  }

  //  void QPlainTextEdit::keyReleaseEvent(QKeyEvent *e)
  void keyReleaseEvent(QKeyEvent *e) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlainTextEditCall5 call = reinterpret_cast<CuteQPlainTextEditCall5>(taken[5]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::keyReleaseEvent(e);
  }

  //  void QPlainTextEdit::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlainTextEditCall6 call = reinterpret_cast<CuteQPlainTextEditCall6>(taken[6]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::resizeEvent(e);
  }

  //  void QPlainTextEdit::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlainTextEditCall7 call = reinterpret_cast<CuteQPlainTextEditCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::paintEvent(e);
  }

  //  void QPlainTextEdit::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlainTextEditCall8 call = reinterpret_cast<CuteQPlainTextEditCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::mousePressEvent(e);
  }

  //  void QPlainTextEdit::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlainTextEditCall9 call = reinterpret_cast<CuteQPlainTextEditCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::mouseMoveEvent(e);
  }

  //  void QPlainTextEdit::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlainTextEditCall10 call = reinterpret_cast<CuteQPlainTextEditCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::mouseReleaseEvent(e);
  }

  //  void QPlainTextEdit::mouseDoubleClickEvent(QMouseEvent *e)
  void mouseDoubleClickEvent(QMouseEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlainTextEditCall11 call = reinterpret_cast<CuteQPlainTextEditCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::mouseDoubleClickEvent(e);
  }

  //  bool QPlainTextEdit::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlainTextEditCall12 call = reinterpret_cast<CuteQPlainTextEditCall12>(taken[12]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QPlainTextEdit::focusNextPrevChild(next);
  }

  //  void QPlainTextEdit::contextMenuEvent(QContextMenuEvent *e)
  void contextMenuEvent(QContextMenuEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlainTextEditCall13 call = reinterpret_cast<CuteQPlainTextEditCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::contextMenuEvent(e);
  }

  //  void QPlainTextEdit::dragEnterEvent(QDragEnterEvent *e)
  void dragEnterEvent(QDragEnterEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlainTextEditCall14 call = reinterpret_cast<CuteQPlainTextEditCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::dragEnterEvent(e);
  }

  //  void QPlainTextEdit::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlainTextEditCall15 call = reinterpret_cast<CuteQPlainTextEditCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::dragLeaveEvent(e);
  }

  //  void QPlainTextEdit::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlainTextEditCall16 call = reinterpret_cast<CuteQPlainTextEditCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::dragMoveEvent(e);
  }

  //  void QPlainTextEdit::dropEvent(QDropEvent *e)
  void dropEvent(QDropEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlainTextEditCall17 call = reinterpret_cast<CuteQPlainTextEditCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::dropEvent(e);
  }

  //  void QPlainTextEdit::focusInEvent(QFocusEvent *e)
  void focusInEvent(QFocusEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlainTextEditCall18 call = reinterpret_cast<CuteQPlainTextEditCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::focusInEvent(e);
  }

  //  void QPlainTextEdit::focusOutEvent(QFocusEvent *e)
  void focusOutEvent(QFocusEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlainTextEditCall19 call = reinterpret_cast<CuteQPlainTextEditCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::focusOutEvent(e);
  }

  //  void QPlainTextEdit::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlainTextEditCall20 call = reinterpret_cast<CuteQPlainTextEditCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlainTextEdit::showEvent(a0);
  }

  //  void QPlainTextEdit::changeEvent(QEvent *e)
  void changeEvent(QEvent *e) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlainTextEditCall21 call = reinterpret_cast<CuteQPlainTextEditCall21>(taken[21]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::changeEvent(e);
  }

  //  void QPlainTextEdit::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPlainTextEditCall22 call = reinterpret_cast<CuteQPlainTextEditCall22>(taken[22]);
      call(this, e, &handled);
      if (handled) return;
    }
    QPlainTextEdit::wheelEvent(e);
  }

  //  QMimeData *QPlainTextEdit::createMimeDataFromSelection() const
  QMimeData *createMimeDataFromSelection() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQPlainTextEditCall23 call = reinterpret_cast<CuteQPlainTextEditCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMimeData *>(given);
    }
    return QPlainTextEdit::createMimeDataFromSelection();
  }

  //  bool QPlainTextEdit::canInsertFromMimeData(const QMimeData *source)
  //      const
  bool canInsertFromMimeData(const QMimeData *source) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQPlainTextEditCall24 call = reinterpret_cast<CuteQPlainTextEditCall24>(taken[24]);
      bool given = call(this, source, &handled);
      if (handled) return given;
    }
    return QPlainTextEdit::canInsertFromMimeData(source);
  }

  //  void QPlainTextEdit::insertFromMimeData(const QMimeData *source)
  void insertFromMimeData(const QMimeData *source) override {
    if (taken[25]) {
      int handled = 0;
      CuteQPlainTextEditCall25 call = reinterpret_cast<CuteQPlainTextEditCall25>(taken[25]);
      call(this, source, &handled);
      if (handled) return;
    }
    QPlainTextEdit::insertFromMimeData(source);
  }

  //  void QPlainTextEdit::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQPlainTextEditCall26 call = reinterpret_cast<CuteQPlainTextEditCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlainTextEdit::inputMethodEvent(a0);
  }

  //  void QPlainTextEdit::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[27]) {
      int handled = 0;
      CuteQPlainTextEditCall27 call = reinterpret_cast<CuteQPlainTextEditCall27>(taken[27]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QPlainTextEdit::scrollContentsBy(dx, dy);
  }

  //  void QPlainTextEdit::doSetTextCursor(const QTextCursor &cursor)
  void doSetTextCursor(const QTextCursor &cursor) override {
    if (taken[28]) {
      int handled = 0;
      CuteQPlainTextEditCall28 call = reinterpret_cast<CuteQPlainTextEditCall28>(taken[28]);
      call(this, &cursor, &handled);
      if (handled) return;
    }
    QPlainTextEdit::doSetTextCursor(cursor);
  }

  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQPlainTextEditCall29 call = reinterpret_cast<CuteQPlainTextEditCall29>(taken[29]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }

  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQPlainTextEditCall30 call = reinterpret_cast<CuteQPlainTextEditCall30>(taken[30]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }

  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[31]) {
      int handled = 0;
      CuteQPlainTextEditCall31 call = reinterpret_cast<CuteQPlainTextEditCall31>(taken[31]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }

  //  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQPlainTextEditCall32 call = reinterpret_cast<CuteQPlainTextEditCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::eventFilter(a0, a1);
  }

  //  bool QAbstractScrollArea::viewportEvent(QEvent *a0)
  bool viewportEvent(QEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQPlainTextEditCall33 call = reinterpret_cast<CuteQPlainTextEditCall33>(taken[33]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractScrollArea::viewportEvent(a0);
  }

  //  QSize QAbstractScrollArea::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQPlainTextEditCall34 call = reinterpret_cast<CuteQPlainTextEditCall34>(taken[34]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::viewportSizeHint();
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQPlainTextEditCall35 call = reinterpret_cast<CuteQPlainTextEditCall35>(taken[35]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQPlainTextEditCall36 call = reinterpret_cast<CuteQPlainTextEditCall36>(taken[36]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[37]) {
      int handled = 0;
      CuteQPlainTextEditCall37 call = reinterpret_cast<CuteQPlainTextEditCall37>(taken[37]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQPlainTextEditCall38 call = reinterpret_cast<CuteQPlainTextEditCall38>(taken[38]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQPlainTextEditCall39 call = reinterpret_cast<CuteQPlainTextEditCall39>(taken[39]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQPlainTextEditCall40 call = reinterpret_cast<CuteQPlainTextEditCall40>(taken[40]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQPlainTextEditCall41 call = reinterpret_cast<CuteQPlainTextEditCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQPlainTextEditCall42 call = reinterpret_cast<CuteQPlainTextEditCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQPlainTextEditCall43 call = reinterpret_cast<CuteQPlainTextEditCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQPlainTextEditCall44 call = reinterpret_cast<CuteQPlainTextEditCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQPlainTextEditCall45 call = reinterpret_cast<CuteQPlainTextEditCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQPlainTextEditCall46 call = reinterpret_cast<CuteQPlainTextEditCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQPlainTextEditCall47 call = reinterpret_cast<CuteQPlainTextEditCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[48]) {
      int handled = 0;
      CuteQPlainTextEditCall48 call = reinterpret_cast<CuteQPlainTextEditCall48>(taken[48]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[49]) {
      int handled = 0;
      CuteQPlainTextEditCall49 call = reinterpret_cast<CuteQPlainTextEditCall49>(taken[49]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[50]) {
      int handled = 0;
      CuteQPlainTextEditCall50 call = reinterpret_cast<CuteQPlainTextEditCall50>(taken[50]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[51]) {
      int handled = 0;
      CuteQPlainTextEditCall51 call = reinterpret_cast<CuteQPlainTextEditCall51>(taken[51]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQPlainTextEditCall52 call = reinterpret_cast<CuteQPlainTextEditCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQPlainTextEditCall53 call = reinterpret_cast<CuteQPlainTextEditCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[54]) {
      int handled = 0;
      CuteQPlainTextEditCall54 call = reinterpret_cast<CuteQPlainTextEditCall54>(taken[54]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[55]) {
      int handled = 0;
      CuteQPlainTextEditCall55 call = reinterpret_cast<CuteQPlainTextEditCall55>(taken[55]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QPlainTextEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QPlainTextEdit10metaObjectEv(
    const QPlainTextEdit *self) {
  return self->metaObject();
}

//  QString QPlainTextEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QPlainTextEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlainTextEdit::tr(s, c, n));
}

//  QPlainTextEdit::QPlainTextEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QPlainTextEdit *ritual_ZN14QPlainTextEditC1EP7QWidget(QWidget *parent) {
  return new CuteQPlainTextEdit(parent);
}

//  QPlainTextEdit::QPlainTextEdit(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QPlainTextEdit *ritual_ZN14QPlainTextEditC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new CuteQPlainTextEdit(*text, parent);
}

//  QPlainTextEdit::~QPlainTextEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEditD1Ev(QPlainTextEdit *self) {
  delete self;
}

//  void QPlainTextEdit::setDocument(QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit11setDocumentEP13QTextDocument(
    QPlainTextEdit *self,
    QTextDocument *document) {
  self->setDocument(document);
}

//  QTextDocument *QPlainTextEdit::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK14QPlainTextEdit8documentEv(
    const QPlainTextEdit *self) {
  return self->document();
}

//  void QPlainTextEdit::setPlaceholderText(const QString &placeholderText)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit18setPlaceholderTextERK7QString(
    QPlainTextEdit *self,
    const QString *placeholderText) {
  self->setPlaceholderText(*placeholderText);
}

//  QString QPlainTextEdit::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlainTextEdit15placeholderTextEv(
    const QPlainTextEdit *self) {
  return new QString(self->placeholderText());
}

//  void QPlainTextEdit::setTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit13setTextCursorERK11QTextCursor(
    QPlainTextEdit *self,
    const QTextCursor *cursor) {
  self->setTextCursor(*cursor);
}

//  QTextCursor QPlainTextEdit::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK14QPlainTextEdit10textCursorEv(
    const QPlainTextEdit *self) {
  return new QTextCursor(self->textCursor());
}

//  bool QPlainTextEdit::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit10isReadOnlyEv(const QPlainTextEdit *self) {
  return self->isReadOnly();
}

//  void QPlainTextEdit::setReadOnly(bool ro)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit11setReadOnlyEb(
    QPlainTextEdit *self,
    bool ro) {
  self->setReadOnly(ro);
}

//  void QPlainTextEdit::setTextInteractionFlags(Qt::TextInteractionFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QPlainTextEdit *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QPlainTextEdit::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QPlainTextEdit20textInteractionFlagsEv(
    const QPlainTextEdit *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QPlainTextEdit::mergeCurrentCharFormat(const QTextCharFormat
//      &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit22mergeCurrentCharFormatERK15QTextCharFormat(
    QPlainTextEdit *self,
    const QTextCharFormat *modifier) {
  self->mergeCurrentCharFormat(*modifier);
}

//  void QPlainTextEdit::setCurrentCharFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit20setCurrentCharFormatERK15QTextCharFormat(
    QPlainTextEdit *self,
    const QTextCharFormat *format) {
  self->setCurrentCharFormat(*format);
}

//  QTextCharFormat QPlainTextEdit::currentCharFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK14QPlainTextEdit17currentCharFormatEv(
    const QPlainTextEdit *self) {
  return new QTextCharFormat(self->currentCharFormat());
}

//  bool QPlainTextEdit::tabChangesFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit15tabChangesFocusEv(
    const QPlainTextEdit *self) {
  return self->tabChangesFocus();
}

//  void QPlainTextEdit::setTabChangesFocus(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit18setTabChangesFocusEb(
    QPlainTextEdit *self,
    bool b) {
  self->setTabChangesFocus(b);
}

//  void QPlainTextEdit::setDocumentTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit16setDocumentTitleERK7QString(
    QPlainTextEdit *self,
    const QString *title) {
  self->setDocumentTitle(*title);
}

//  QString QPlainTextEdit::documentTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlainTextEdit13documentTitleEv(
    const QPlainTextEdit *self) {
  return new QString(self->documentTitle());
}

//  bool QPlainTextEdit::isUndoRedoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit17isUndoRedoEnabledEv(
    const QPlainTextEdit *self) {
  return self->isUndoRedoEnabled();
}

//  void QPlainTextEdit::setUndoRedoEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit18setUndoRedoEnabledEb(
    QPlainTextEdit *self,
    bool enable) {
  self->setUndoRedoEnabled(enable);
}

//  void QPlainTextEdit::setMaximumBlockCount(int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit20setMaximumBlockCountEi(
    QPlainTextEdit *self,
    int maximum) {
  self->setMaximumBlockCount(maximum);
}

//  int QPlainTextEdit::maximumBlockCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QPlainTextEdit17maximumBlockCountEv(
    const QPlainTextEdit *self) {
  return self->maximumBlockCount();
}

//  LineWrapMode QPlainTextEdit::lineWrapMode() const
extern "C" Q_DECL_EXPORT
QPlainTextEdit::LineWrapMode ritual_ZNK14QPlainTextEdit12lineWrapModeEv(
    const QPlainTextEdit *self) {
  return self->lineWrapMode();
}

//  void QPlainTextEdit::setLineWrapMode(LineWrapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit15setLineWrapModeENS_12LineWrapModeE(
    QPlainTextEdit *self,
    QPlainTextEdit::LineWrapMode mode) {
  self->setLineWrapMode(mode);
}

//  QTextOption::WrapMode QPlainTextEdit::wordWrapMode() const
extern "C" Q_DECL_EXPORT
QTextOption::WrapMode ritual_ZNK14QPlainTextEdit12wordWrapModeEv(
    const QPlainTextEdit *self) {
  return self->wordWrapMode();
}

//  void QPlainTextEdit::setWordWrapMode(QTextOption::WrapMode policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit15setWordWrapModeEN11QTextOption8WrapModeE(
    QPlainTextEdit *self,
    QTextOption::WrapMode policy) {
  self->setWordWrapMode(policy);
}

//  void QPlainTextEdit::setBackgroundVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit20setBackgroundVisibleEb(
    QPlainTextEdit *self,
    bool visible) {
  self->setBackgroundVisible(visible);
}

//  bool QPlainTextEdit::backgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit17backgroundVisibleEv(
    const QPlainTextEdit *self) {
  return self->backgroundVisible();
}

//  void QPlainTextEdit::setCenterOnScroll(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit17setCenterOnScrollEb(
    QPlainTextEdit *self,
    bool enabled) {
  self->setCenterOnScroll(enabled);
}

//  bool QPlainTextEdit::centerOnScroll() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit14centerOnScrollEv(
    const QPlainTextEdit *self) {
  return self->centerOnScroll();
}

//  bool QPlainTextEdit::find(const QString &exp, QTextDocument::FindFlags
//      options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QPlainTextEdit4findERK7QString6QFlagsIN13QTextDocument8FindFlagEE(
    QPlainTextEdit *self,
    const QString *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}

//  bool QPlainTextEdit::find(const QRegularExpression &exp,
//      QTextDocument::FindFlags options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QPlainTextEdit4findERK18QRegularExpression6QFlagsIN13QTextDocument8FindFlagEE(
    QPlainTextEdit *self,
    const QRegularExpression *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}

//  QString QPlainTextEdit::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlainTextEdit11toPlainTextEv(
    const QPlainTextEdit *self) {
  return new QString(self->toPlainText());
}

//  void QPlainTextEdit::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit19ensureCursorVisibleEv(QPlainTextEdit *self) {
  self->ensureCursorVisible();
}

//  QVariant QPlainTextEdit::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QPlainTextEdit12loadResourceEiRK4QUrl(
    QPlainTextEdit *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

//  QMenu *QPlainTextEdit::createStandardContextMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN14QPlainTextEdit25createStandardContextMenuEv(
    QPlainTextEdit *self) {
  return self->createStandardContextMenu();
}

//  QMenu *QPlainTextEdit::createStandardContextMenu(const QPoint &position)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN14QPlainTextEdit25createStandardContextMenuERK6QPoint(
    QPlainTextEdit *self,
    const QPoint *position) {
  return self->createStandardContextMenu(*position);
}

//  QTextCursor QPlainTextEdit::cursorForPosition(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK14QPlainTextEdit17cursorForPositionERK6QPoint(
    const QPlainTextEdit *self,
    const QPoint *pos) {
  return new QTextCursor(self->cursorForPosition(*pos));
}

//  QRect QPlainTextEdit::cursorRect(const QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QPlainTextEdit10cursorRectERK11QTextCursor(
    const QPlainTextEdit *self,
    const QTextCursor *cursor) {
  return new QRect(self->cursorRect(*cursor));
}

//  QRect QPlainTextEdit::cursorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QPlainTextEdit10cursorRectEv(const QPlainTextEdit *self) {
  return new QRect(self->cursorRect());
}

//  QString QPlainTextEdit::anchorAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlainTextEdit8anchorAtERK6QPoint(
    const QPlainTextEdit *self,
    const QPoint *pos) {
  return new QString(self->anchorAt(*pos));
}

//  bool QPlainTextEdit::overwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit13overwriteModeEv(
    const QPlainTextEdit *self) {
  return self->overwriteMode();
}

//  void QPlainTextEdit::setOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit16setOverwriteModeEb(
    QPlainTextEdit *self,
    bool overwrite) {
  self->setOverwriteMode(overwrite);
}

//  qreal QPlainTextEdit::tabStopDistance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QPlainTextEdit15tabStopDistanceEv(
    const QPlainTextEdit *self) {
  return self->tabStopDistance();
}

//  void QPlainTextEdit::setTabStopDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit18setTabStopDistanceEd(
    QPlainTextEdit *self,
    qreal distance) {
  self->setTabStopDistance(distance);
}

//  int QPlainTextEdit::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QPlainTextEdit11cursorWidthEv(const QPlainTextEdit *self) {
  return self->cursorWidth();
}

//  void QPlainTextEdit::setCursorWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit14setCursorWidthEi(
    QPlainTextEdit *self,
    int width) {
  self->setCursorWidth(width);
}

//  void QPlainTextEdit::moveCursor(QTextCursor::MoveOperation operation,
//      QTextCursor::MoveMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit10moveCursorEN11QTextCursor13MoveOperationENS0_8MoveModeE(
    QPlainTextEdit *self,
    QTextCursor::MoveOperation operation,
    QTextCursor::MoveMode mode) {
  self->moveCursor(operation, mode);
}

//  bool QPlainTextEdit::canPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit8canPasteEv(const QPlainTextEdit *self) {
  return self->canPaste();
}

//  void QPlainTextEdit::print(QPagedPaintDevice *printer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QPlainTextEdit5printEP17QPagedPaintDevice(
    const QPlainTextEdit *self,
    QPagedPaintDevice *printer) {
  self->print(printer);
}

//  int QPlainTextEdit::blockCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QPlainTextEdit10blockCountEv(const QPlainTextEdit *self) {
  return self->blockCount();
}

//  QVariant QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QPlainTextEdit *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->inputMethodQuery(property));
}

//  QVariant QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery query,
//      QVariant argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QPlainTextEdit *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}

//  void QPlainTextEdit::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit12setPlainTextERK7QString(
    QPlainTextEdit *self,
    const QString *text) {
  self->setPlainText(*text);
}

//  void QPlainTextEdit::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit3cutEv(QPlainTextEdit *self) {
  self->cut();
}

//  void QPlainTextEdit::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit4copyEv(QPlainTextEdit *self) {
  self->copy();
}

//  void QPlainTextEdit::paste()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit5pasteEv(QPlainTextEdit *self) {
  self->paste();
}

//  void QPlainTextEdit::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit4undoEv(QPlainTextEdit *self) {
  self->undo();
}

//  void QPlainTextEdit::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit4redoEv(QPlainTextEdit *self) {
  self->redo();
}

//  void QPlainTextEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit5clearEv(QPlainTextEdit *self) {
  self->clear();
}

//  void QPlainTextEdit::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit9selectAllEv(QPlainTextEdit *self) {
  self->selectAll();
}

//  void QPlainTextEdit::insertPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit15insertPlainTextERK7QString(
    QPlainTextEdit *self,
    const QString *text) {
  self->insertPlainText(*text);
}

//  void QPlainTextEdit::appendPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit15appendPlainTextERK7QString(
    QPlainTextEdit *self,
    const QString *text) {
  self->appendPlainText(*text);
}

//  void QPlainTextEdit::appendHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit10appendHtmlERK7QString(
    QPlainTextEdit *self,
    const QString *html) {
  self->appendHtml(*html);
}

//  void QPlainTextEdit::centerCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit12centerCursorEv(QPlainTextEdit *self) {
  self->centerCursor();
}

//  void QPlainTextEdit::zoomIn(int range)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit6zoomInEi(QPlainTextEdit *self, int range) {
  self->zoomIn(range);
}

//  void QPlainTextEdit::zoomOut(int range)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit7zoomOutEi(QPlainTextEdit *self, int range) {
  self->zoomOut(range);
}

//  a Python function taken by a CuteQPlainTextEdit, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlainTextEdit(
    QPlainTextEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlainTextEdit *>(self)->take(key, call);
}

//  QVariant QPlainTextEdit::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN14QPlainTextEdit12loadResourceEiRK4QUrl(
    QPlainTextEdit *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->QPlainTextEdit::loadResource(type, *name));
}

//  QVariant QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QPlainTextEdit *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->QPlainTextEdit::inputMethodQuery(property));
}

//  bool QPlainTextEdit::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QPlainTextEdit5eventEP6QEvent(
    QPlainTextEdit *self,
    QEvent *e) {
  return static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::event(e);
}

//  void QPlainTextEdit::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit10timerEventEP11QTimerEvent(
    QPlainTextEdit *self,
    QTimerEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::timerEvent(e);
}

//  void QPlainTextEdit::keyPressEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit13keyPressEventEP9QKeyEvent(
    QPlainTextEdit *self,
    QKeyEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::keyPressEvent(
      e);
}

//  void QPlainTextEdit::keyReleaseEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit15keyReleaseEventEP9QKeyEvent(
    QPlainTextEdit *self,
    QKeyEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::keyReleaseEvent(
      e);
}

//  void QPlainTextEdit::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit11resizeEventEP12QResizeEvent(
    QPlainTextEdit *self,
    QResizeEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::resizeEvent(e);
}

//  void QPlainTextEdit::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit10paintEventEP11QPaintEvent(
    QPlainTextEdit *self,
    QPaintEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::paintEvent(e);
}

//  void QPlainTextEdit::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit15mousePressEventEP11QMouseEvent(
    QPlainTextEdit *self,
    QMouseEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::mousePressEvent(
      e);
}

//  void QPlainTextEdit::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit14mouseMoveEventEP11QMouseEvent(
    QPlainTextEdit *self,
    QMouseEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::mouseMoveEvent(
      e);
}

//  void QPlainTextEdit::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit17mouseReleaseEventEP11QMouseEvent(
    QPlainTextEdit *self,
    QMouseEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::mouseReleaseEvent(
      e);
}

//  void QPlainTextEdit::mouseDoubleClickEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit21mouseDoubleClickEventEP11QMouseEvent(
    QPlainTextEdit *self,
    QMouseEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::mouseDoubleClickEvent(
      e);
}

//  bool QPlainTextEdit::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QPlainTextEdit18focusNextPrevChildEb(
    QPlainTextEdit *self,
    bool next) {
  return static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::focusNextPrevChild(
      next);
}

//  void QPlainTextEdit::contextMenuEvent(QContextMenuEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit16contextMenuEventEP17QContextMenuEvent(
    QPlainTextEdit *self,
    QContextMenuEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::contextMenuEvent(
      e);
}

//  void QPlainTextEdit::dragEnterEvent(QDragEnterEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit14dragEnterEventEP15QDragEnterEvent(
    QPlainTextEdit *self,
    QDragEnterEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::dragEnterEvent(
      e);
}

//  void QPlainTextEdit::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit14dragLeaveEventEP15QDragLeaveEvent(
    QPlainTextEdit *self,
    QDragLeaveEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::dragLeaveEvent(
      e);
}

//  void QPlainTextEdit::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit13dragMoveEventEP14QDragMoveEvent(
    QPlainTextEdit *self,
    QDragMoveEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::dragMoveEvent(
      e);
}

//  void QPlainTextEdit::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit9dropEventEP10QDropEvent(
    QPlainTextEdit *self,
    QDropEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::dropEvent(e);
}

//  void QPlainTextEdit::focusInEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit12focusInEventEP11QFocusEvent(
    QPlainTextEdit *self,
    QFocusEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::focusInEvent(e);
}

//  void QPlainTextEdit::focusOutEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit13focusOutEventEP11QFocusEvent(
    QPlainTextEdit *self,
    QFocusEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::focusOutEvent(
      e);
}

//  void QPlainTextEdit::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit9showEventEP10QShowEvent(
    QPlainTextEdit *self,
    QShowEvent *a0) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::showEvent(a0);
}

//  void QPlainTextEdit::changeEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit11changeEventEP6QEvent(
    QPlainTextEdit *self,
    QEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::changeEvent(e);
}

//  void QPlainTextEdit::wheelEvent(QWheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit10wheelEventEP11QWheelEvent(
    QPlainTextEdit *self,
    QWheelEvent *e) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::wheelEvent(e);
}

//  QMimeData *QPlainTextEdit::createMimeDataFromSelection() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_own_ZNK14QPlainTextEdit27createMimeDataFromSelectionEv(
    const QPlainTextEdit *self) {
  return static_cast<const OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::createMimeDataFromSelection();
}

//  bool QPlainTextEdit::canInsertFromMimeData(const QMimeData *source) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QPlainTextEdit21canInsertFromMimeDataEPK9QMimeData(
    const QPlainTextEdit *self,
    const QMimeData *source) {
  return static_cast<const OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::canInsertFromMimeData(
      source);
}

//  void QPlainTextEdit::insertFromMimeData(const QMimeData *source)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit18insertFromMimeDataEPK9QMimeData(
    QPlainTextEdit *self,
    const QMimeData *source) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::insertFromMimeData(
      source);
}

//  void QPlainTextEdit::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit16inputMethodEventEP17QInputMethodEvent(
    QPlainTextEdit *self,
    QInputMethodEvent *a0) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::inputMethodEvent(
      a0);
}

//  void QPlainTextEdit::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit16scrollContentsByEii(
    QPlainTextEdit *self,
    int dx,
    int dy) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::scrollContentsBy(
      dx,
      dy);
}

//  void QPlainTextEdit::doSetTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QPlainTextEdit15doSetTextCursorERK11QTextCursor(
    QPlainTextEdit *self,
    const QTextCursor *cursor) {
  static_cast<OwnQPlainTextEdit *>(self)->OwnQPlainTextEdit::doSetTextCursor(
      *cursor);
}
