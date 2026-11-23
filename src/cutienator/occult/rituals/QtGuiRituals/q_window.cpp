//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qwindow.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qpoint.h>
#include <QtGui/qicon.h>
#include <QtGui/qcursor.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWindow : QWindow {
  using QWindow::exposeEvent;
  using QWindow::resizeEvent;
  using QWindow::paintEvent;
  using QWindow::moveEvent;
  using QWindow::focusInEvent;
  using QWindow::focusOutEvent;
  using QWindow::showEvent;
  using QWindow::hideEvent;
  using QWindow::closeEvent;
  using QWindow::event;
  using QWindow::keyPressEvent;
  using QWindow::keyReleaseEvent;
  using QWindow::mousePressEvent;
  using QWindow::mouseReleaseEvent;
  using QWindow::mouseDoubleClickEvent;
  using QWindow::mouseMoveEvent;
  using QWindow::wheelEvent;
  using QWindow::touchEvent;
  using QWindow::tabletEvent;
};

//  A QWindow that Python can take functions over in. Every QWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQWindowCall0)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQWindowCall1)(const void *, int *);
typedef const QSize * (*CuteQWindowCall2)(const void *, int *);
typedef void * (*CuteQWindowCall3)(const void *, int *);
typedef void * (*CuteQWindowCall4)(const void *, int *);
typedef void (*CuteQWindowCall5)(const void *, QExposeEvent *, int *);
typedef void (*CuteQWindowCall6)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWindowCall7)(const void *, QPaintEvent *, int *);
typedef void (*CuteQWindowCall8)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWindowCall9)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWindowCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWindowCall11)(const void *, QShowEvent *, int *);
typedef void (*CuteQWindowCall12)(const void *, QHideEvent *, int *);
typedef void (*CuteQWindowCall13)(const void *, QCloseEvent *, int *);
typedef bool (*CuteQWindowCall14)(const void *, QEvent *, int *);
typedef void (*CuteQWindowCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWindowCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWindowCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWindowCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWindowCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWindowCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWindowCall21)(const void *, QWheelEvent *, int *);
typedef void (*CuteQWindowCall22)(const void *, QTouchEvent *, int *);
typedef void (*CuteQWindowCall23)(const void *, QTabletEvent *, int *);
typedef bool (*CuteQWindowCall24)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQWindowCall25)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWindowCall26)(const void *, QChildEvent *, int *);
typedef void (*CuteQWindowCall27)(const void *, QEvent *, int *);
typedef void (*CuteQWindowCall28)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWindowCall29)(const void *, const QMetaMethod *, int *);
class CuteQWindow : public QWindow {
public:
  using QWindow::QWindow;
  void *taken[30] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[29] = call;
      return true;
    }
    return false;
  }

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowCall0 call = reinterpret_cast<CuteQWindowCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowCall1 call = reinterpret_cast<CuteQWindowCall1>(taken[1]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowCall2 call = reinterpret_cast<CuteQWindowCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  QAccessibleInterface *QWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowCall3 call = reinterpret_cast<CuteQWindowCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWindow::accessibleRoot();
  }

  //  QObject *QWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowCall4 call = reinterpret_cast<CuteQWindowCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWindow::focusObject();
  }

  //  void QWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowCall5 call = reinterpret_cast<CuteQWindowCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::exposeEvent(a0);
  }

  //  void QWindow::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowCall6 call = reinterpret_cast<CuteQWindowCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::resizeEvent(a0);
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowCall7 call = reinterpret_cast<CuteQWindowCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowCall8 call = reinterpret_cast<CuteQWindowCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWindowCall9 call = reinterpret_cast<CuteQWindowCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWindowCall10 call = reinterpret_cast<CuteQWindowCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWindowCall11 call = reinterpret_cast<CuteQWindowCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWindowCall12 call = reinterpret_cast<CuteQWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWindowCall13 call = reinterpret_cast<CuteQWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::closeEvent(a0);
  }

  //  bool QWindow::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWindowCall14 call = reinterpret_cast<CuteQWindowCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWindow::event(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWindowCall15 call = reinterpret_cast<CuteQWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWindowCall16 call = reinterpret_cast<CuteQWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWindowCall17 call = reinterpret_cast<CuteQWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWindowCall18 call = reinterpret_cast<CuteQWindowCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWindowCall19 call = reinterpret_cast<CuteQWindowCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWindowCall20 call = reinterpret_cast<CuteQWindowCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseMoveEvent(a0);
  }

  //  void QWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWindowCall21 call = reinterpret_cast<CuteQWindowCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::wheelEvent(a0);
  }

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWindowCall22 call = reinterpret_cast<CuteQWindowCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWindowCall23 call = reinterpret_cast<CuteQWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQWindowCall24 call = reinterpret_cast<CuteQWindowCall24>(taken[24]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWindowCall25 call = reinterpret_cast<CuteQWindowCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWindowCall26 call = reinterpret_cast<CuteQWindowCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWindowCall27 call = reinterpret_cast<CuteQWindowCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWindowCall28 call = reinterpret_cast<CuteQWindowCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWindowCall29 call = reinterpret_cast<CuteQWindowCall29>(taken[29]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QWindow10metaObjectEv(const QWindow *self) {
  return self->metaObject();
}

//  QString QWindow::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QWindow2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QWindow::tr(s, c, n));
}

//  QWindow::QWindow(QScreen *screen)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN7QWindowC1EP7QScreen(QScreen *screen) {
  return new CuteQWindow(screen);
}

//  QWindow::QWindow(QWindow *parent)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN7QWindowC1EPS_(QWindow *parent) {
  return new CuteQWindow(parent);
}

//  QWindow::~QWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindowD1Ev(QWindow *self) {
  delete self;
}

//  void QWindow::setSurfaceType(SurfaceType surfaceType)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14setSurfaceTypeEN8QSurface11SurfaceTypeE(
    QWindow *self,
    QSurface::SurfaceType surfaceType) {
  self->setSurfaceType(surfaceType);
}

//  SurfaceType QWindow::surfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK7QWindow11surfaceTypeEv(
    const QWindow *self) {
  return self->surfaceType();
}

//  bool QWindow::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow9isVisibleEv(const QWindow *self) {
  return self->isVisible();
}

//  Visibility QWindow::visibility() const
extern "C" Q_DECL_EXPORT
QWindow::Visibility ritual_ZNK7QWindow10visibilityEv(const QWindow *self) {
  return self->visibility();
}

//  void QWindow::setVisibility(Visibility v)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13setVisibilityENS_10VisibilityE(
    QWindow *self,
    QWindow::Visibility v) {
  self->setVisibility(v);
}

//  void QWindow::create()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow6createEv(QWindow *self) {
  self->create();
}

//  WId QWindow::winId() const
extern "C" Q_DECL_EXPORT
WId ritual_ZNK7QWindow5winIdEv(const QWindow *self) {
  return self->winId();
}

//  QWindow *QWindow::parent(AncestorMode mode) const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK7QWindow6parentENS_12AncestorModeE(
    const QWindow *self,
    QWindow::AncestorMode mode) {
  return self->parent(mode);
}

//  void QWindow::setParent(QWindow *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setParentEPS_(QWindow *self, QWindow *parent) {
  self->setParent(parent);
}

//  bool QWindow::isTopLevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow10isTopLevelEv(const QWindow *self) {
  return self->isTopLevel();
}

//  bool QWindow::isModal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow7isModalEv(const QWindow *self) {
  return self->isModal();
}

//  Qt::WindowModality QWindow::modality() const
extern "C" Q_DECL_EXPORT
Qt::WindowModality ritual_ZNK7QWindow8modalityEv(const QWindow *self) {
  return self->modality();
}

//  void QWindow::setModality(Qt::WindowModality modality)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setModalityEN2Qt14WindowModalityE(
    QWindow *self,
    Qt::WindowModality modality) {
  self->setModality(modality);
}

//  void QWindow::setFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setFormatERK14QSurfaceFormat(
    QWindow *self,
    const QSurfaceFormat *format) {
  self->setFormat(*format);
}

//  QSurfaceFormat QWindow::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK7QWindow6formatEv(const QWindow *self) {
  return new QSurfaceFormat(self->format());
}

//  QSurfaceFormat QWindow::requestedFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK7QWindow15requestedFormatEv(const QWindow *self) {
  return new QSurfaceFormat(self->requestedFormat());
}

//  void QWindow::setFlags(Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow8setFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QWindow *self,
    int flags) {
  self->setFlags(QFlags<Qt::WindowType>::fromInt(flags));
}

//  Qt::WindowFlags QWindow::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow5flagsEv(const QWindow *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QWindow::setFlag(Qt::WindowType a0, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow7setFlagEN2Qt10WindowTypeEb(
    QWindow *self,
    Qt::WindowType a0,
    bool on) {
  self->setFlag(a0, on);
}

//  Qt::WindowType QWindow::type() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_ZNK7QWindow4typeEv(const QWindow *self) {
  return self->type();
}

//  QString QWindow::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWindow5titleEv(const QWindow *self) {
  return new QString(self->title());
}

//  void QWindow::setOpacity(qreal level)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10setOpacityEd(QWindow *self, qreal level) {
  self->setOpacity(level);
}

//  qreal QWindow::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QWindow7opacityEv(const QWindow *self) {
  return self->opacity();
}

//  void QWindow::setMask(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow7setMaskERK7QRegion(
    QWindow *self,
    const QRegion *region) {
  self->setMask(*region);
}

//  QRegion QWindow::mask() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QWindow4maskEv(const QWindow *self) {
  return new QRegion(self->mask());
}

//  bool QWindow::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow8isActiveEv(const QWindow *self) {
  return self->isActive();
}

//  void QWindow::reportContentOrientationChange(Qt::ScreenOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow30reportContentOrientationChangeEN2Qt17ScreenOrientationE(
    QWindow *self,
    Qt::ScreenOrientation orientation) {
  self->reportContentOrientationChange(orientation);
}

//  Qt::ScreenOrientation QWindow::contentOrientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK7QWindow18contentOrientationEv(
    const QWindow *self) {
  return self->contentOrientation();
}

//  qreal QWindow::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QWindow16devicePixelRatioEv(const QWindow *self) {
  return self->devicePixelRatio();
}

//  Qt::WindowState QWindow::windowState() const
extern "C" Q_DECL_EXPORT
Qt::WindowState ritual_ZNK7QWindow11windowStateEv(const QWindow *self) {
  return self->windowState();
}

//  Qt::WindowStates QWindow::windowStates() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow12windowStatesEv(const QWindow *self) {
  return static_cast<int>(self->windowStates().toInt());
}

//  void QWindow::setWindowState(Qt::WindowState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14setWindowStateEN2Qt11WindowStateE(
    QWindow *self,
    Qt::WindowState state) {
  self->setWindowState(state);
}

//  void QWindow::setWindowStates(Qt::WindowStates states)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15setWindowStatesE6QFlagsIN2Qt11WindowStateEE(
    QWindow *self,
    int states) {
  self->setWindowStates(QFlags<Qt::WindowState>::fromInt(states));
}

//  void QWindow::setTransientParent(QWindow *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow18setTransientParentEPS_(
    QWindow *self,
    QWindow *parent) {
  self->setTransientParent(parent);
}

//  QWindow *QWindow::transientParent() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK7QWindow15transientParentEv(const QWindow *self) {
  return self->transientParent();
}

//  bool QWindow::isAncestorOf(const QWindow *child, AncestorMode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow12isAncestorOfEPKS_NS_12AncestorModeE(
    const QWindow *self,
    const QWindow *child,
    QWindow::AncestorMode mode) {
  return self->isAncestorOf(child, mode);
}

//  bool QWindow::isExposed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QWindow9isExposedEv(const QWindow *self) {
  return self->isExposed();
}

//  int QWindow::minimumWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow12minimumWidthEv(const QWindow *self) {
  return self->minimumWidth();
}

//  int QWindow::minimumHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow13minimumHeightEv(const QWindow *self) {
  return self->minimumHeight();
}

//  int QWindow::maximumWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow12maximumWidthEv(const QWindow *self) {
  return self->maximumWidth();
}

//  int QWindow::maximumHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow13maximumHeightEv(const QWindow *self) {
  return self->maximumHeight();
}

//  QSize QWindow::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow11minimumSizeEv(const QWindow *self) {
  return new QSize(self->minimumSize());
}

//  QSize QWindow::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow11maximumSizeEv(const QWindow *self) {
  return new QSize(self->maximumSize());
}

//  QSize QWindow::baseSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow8baseSizeEv(const QWindow *self) {
  return new QSize(self->baseSize());
}

//  QSize QWindow::sizeIncrement() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow13sizeIncrementEv(const QWindow *self) {
  return new QSize(self->sizeIncrement());
}

//  void QWindow::setMinimumSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14setMinimumSizeERK5QSize(
    QWindow *self,
    const QSize *size) {
  self->setMinimumSize(*size);
}

//  void QWindow::setMaximumSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14setMaximumSizeERK5QSize(
    QWindow *self,
    const QSize *size) {
  self->setMaximumSize(*size);
}

//  void QWindow::setBaseSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setBaseSizeERK5QSize(
    QWindow *self,
    const QSize *size) {
  self->setBaseSize(*size);
}

//  void QWindow::setSizeIncrement(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setSizeIncrementERK5QSize(
    QWindow *self,
    const QSize *size) {
  self->setSizeIncrement(*size);
}

//  QRect QWindow::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWindow8geometryEv(const QWindow *self) {
  return new QRect(self->geometry());
}

//  QMargins QWindow::frameMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK7QWindow12frameMarginsEv(const QWindow *self) {
  return new QMargins(self->frameMargins());
}

//  QRect QWindow::frameGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QWindow13frameGeometryEv(const QWindow *self) {
  return new QRect(self->frameGeometry());
}

//  QPoint QWindow::framePosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWindow13framePositionEv(const QWindow *self) {
  return new QPoint(self->framePosition());
}

//  void QWindow::setFramePosition(const QPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setFramePositionERK6QPoint(
    QWindow *self,
    const QPoint *point) {
  self->setFramePosition(*point);
}

//  void QWindow::setFramePosition(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setFramePositionEii(QWindow *self, int x, int y) {
  self->setFramePosition(x, y);
}

//  QMargins QWindow::safeAreaMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK7QWindow15safeAreaMarginsEv(const QWindow *self) {
  return new QMargins(self->safeAreaMargins());
}

//  int QWindow::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow5widthEv(const QWindow *self) {
  return self->width();
}

//  int QWindow::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow6heightEv(const QWindow *self) {
  return self->height();
}

//  int QWindow::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow1xEv(const QWindow *self) {
  return self->x();
}

//  int QWindow::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QWindow1yEv(const QWindow *self) {
  return self->y();
}

//  QSize QWindow::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK7QWindow4sizeEv(const QWindow *self) {
  return new QSize(self->size());
}

//  QPoint QWindow::position() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWindow8positionEv(const QWindow *self) {
  return new QPoint(self->position());
}

//  void QWindow::setPosition(const QPoint &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setPositionERK6QPoint(
    QWindow *self,
    const QPoint *pt) {
  self->setPosition(*pt);
}

//  void QWindow::setPosition(int posx, int posy)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setPositionEii(QWindow *self, int posx, int posy) {
  self->setPosition(posx, posy);
}

//  void QWindow::resize(const QSize &newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow6resizeERK5QSize(QWindow *self, const QSize *newSize) {
  self->resize(*newSize);
}

//  void QWindow::resize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow6resizeEii(QWindow *self, int w, int h) {
  self->resize(w, h);
}

//  void QWindow::setFilePath(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setFilePathERK7QString(
    QWindow *self,
    const QString *filePath) {
  self->setFilePath(*filePath);
}

//  QString QWindow::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QWindow8filePathEv(const QWindow *self) {
  return new QString(self->filePath());
}

//  void QWindow::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow7setIconERK5QIcon(QWindow *self, const QIcon *icon) {
  self->setIcon(*icon);
}

//  QIcon QWindow::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK7QWindow4iconEv(const QWindow *self) {
  return new QIcon(self->icon());
}

//  void QWindow::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow7destroyEv(QWindow *self) {
  self->destroy();
}

//  bool QWindow::setKeyboardGrabEnabled(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow22setKeyboardGrabEnabledEb(QWindow *self, bool grab) {
  return self->setKeyboardGrabEnabled(grab);
}

//  bool QWindow::setMouseGrabEnabled(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow19setMouseGrabEnabledEb(QWindow *self, bool grab) {
  return self->setMouseGrabEnabled(grab);
}

//  QScreen *QWindow::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK7QWindow6screenEv(const QWindow *self) {
  return self->screen();
}

//  void QWindow::setScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setScreenEP7QScreen(QWindow *self, QScreen *screen) {
  self->setScreen(screen);
}

//  QAccessibleInterface *QWindow::accessibleRoot() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK7QWindow14accessibleRootEv(
    const QWindow *self) {
  return self->accessibleRoot();
}

//  QObject *QWindow::focusObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK7QWindow11focusObjectEv(const QWindow *self) {
  return self->focusObject();
}

//  QPointF QWindow::mapToGlobal(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWindow11mapToGlobalERK7QPointF(
    const QWindow *self,
    const QPointF *pos) {
  return new QPointF(self->mapToGlobal(*pos));
}

//  QPointF QWindow::mapFromGlobal(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QWindow13mapFromGlobalERK7QPointF(
    const QWindow *self,
    const QPointF *pos) {
  return new QPointF(self->mapFromGlobal(*pos));
}

//  QPoint QWindow::mapToGlobal(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWindow11mapToGlobalERK6QPoint(
    const QWindow *self,
    const QPoint *pos) {
  return new QPoint(self->mapToGlobal(*pos));
}

//  QPoint QWindow::mapFromGlobal(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QWindow13mapFromGlobalERK6QPoint(
    const QWindow *self,
    const QPoint *pos) {
  return new QPoint(self->mapFromGlobal(*pos));
}

//  QCursor QWindow::cursor() const
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZNK7QWindow6cursorEv(const QWindow *self) {
  return new QCursor(self->cursor());
}

//  void QWindow::setCursor(const QCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setCursorERK7QCursor(
    QWindow *self,
    const QCursor *a0) {
  self->setCursor(*a0);
}

//  void QWindow::unsetCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11unsetCursorEv(QWindow *self) {
  self->unsetCursor();
}

//  QWindow *QWindow::fromWinId(WId id)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN7QWindow9fromWinIdEy(WId id) {
  return QWindow::fromWinId(id);
}

//  void QWindow::requestActivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15requestActivateEv(QWindow *self) {
  self->requestActivate();
}

//  void QWindow::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10setVisibleEb(QWindow *self, bool visible) {
  self->setVisible(visible);
}

//  void QWindow::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow4showEv(QWindow *self) {
  self->show();
}

//  void QWindow::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow4hideEv(QWindow *self) {
  self->hide();
}

//  void QWindow::showMinimized()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13showMinimizedEv(QWindow *self) {
  self->showMinimized();
}

//  void QWindow::showMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13showMaximizedEv(QWindow *self) {
  self->showMaximized();
}

//  void QWindow::showFullScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14showFullScreenEv(QWindow *self) {
  self->showFullScreen();
}

//  void QWindow::showNormal()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10showNormalEv(QWindow *self) {
  self->showNormal();
}

//  bool QWindow::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow5closeEv(QWindow *self) {
  return self->close();
}

//  void QWindow::raise()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow5raiseEv(QWindow *self) {
  self->raise();
}

//  void QWindow::lower()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow5lowerEv(QWindow *self) {
  self->lower();
}

//  bool QWindow::startSystemResize(Qt::Edges edges)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow17startSystemResizeE6QFlagsIN2Qt4EdgeEE(
    QWindow *self,
    int edges) {
  return self->startSystemResize(QFlags<Qt::Edge>::fromInt(edges));
}

//  bool QWindow::startSystemMove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow15startSystemMoveEv(QWindow *self) {
  return self->startSystemMove();
}

//  void QWindow::setTitle(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow8setTitleERK7QString(
    QWindow *self,
    const QString *a0) {
  self->setTitle(*a0);
}

//  void QWindow::setX(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow4setXEi(QWindow *self, int arg) {
  self->setX(arg);
}

//  void QWindow::setY(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow4setYEi(QWindow *self, int arg) {
  self->setY(arg);
}

//  void QWindow::setWidth(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow8setWidthEi(QWindow *self, int arg) {
  self->setWidth(arg);
}

//  void QWindow::setHeight(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9setHeightEi(QWindow *self, int arg) {
  self->setHeight(arg);
}

//  void QWindow::setGeometry(int posx, int posy, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setGeometryEiiii(
    QWindow *self,
    int posx,
    int posy,
    int w,
    int h) {
  self->setGeometry(posx, posy, w, h);
}

//  void QWindow::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11setGeometryERK5QRect(
    QWindow *self,
    const QRect *rect) {
  self->setGeometry(*rect);
}

//  void QWindow::setMinimumWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15setMinimumWidthEi(QWindow *self, int w) {
  self->setMinimumWidth(w);
}

//  void QWindow::setMinimumHeight(int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setMinimumHeightEi(QWindow *self, int h) {
  self->setMinimumHeight(h);
}

//  void QWindow::setMaximumWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15setMaximumWidthEi(QWindow *self, int w) {
  self->setMaximumWidth(w);
}

//  void QWindow::setMaximumHeight(int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow16setMaximumHeightEi(QWindow *self, int h) {
  self->setMaximumHeight(h);
}

//  void QWindow::alert(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow5alertEi(QWindow *self, int msec) {
  self->alert(msec);
}

//  void QWindow::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13requestUpdateEv(QWindow *self) {
  self->requestUpdate();
}

//  void QWindow::exposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11exposeEventEP12QExposeEvent(
    QWindow *self,
    QExposeEvent *a0) {
  self->exposeEvent(a0);
}

//  void QWindow::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11resizeEventEP12QResizeEvent(
    QWindow *self,
    QResizeEvent *a0) {
  self->resizeEvent(a0);
}

//  void QWindow::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10paintEventEP11QPaintEvent(
    QWindow *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QWindow::moveEvent(QMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9moveEventEP10QMoveEvent(
    QWindow *self,
    QMoveEvent *a0) {
  self->moveEvent(a0);
}

//  void QWindow::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow12focusInEventEP11QFocusEvent(
    QWindow *self,
    QFocusEvent *a0) {
  self->focusInEvent(a0);
}

//  void QWindow::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13focusOutEventEP11QFocusEvent(
    QWindow *self,
    QFocusEvent *a0) {
  self->focusOutEvent(a0);
}

//  void QWindow::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9showEventEP10QShowEvent(
    QWindow *self,
    QShowEvent *a0) {
  self->showEvent(a0);
}

//  void QWindow::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow9hideEventEP10QHideEvent(
    QWindow *self,
    QHideEvent *a0) {
  self->hideEvent(a0);
}

//  void QWindow::closeEvent(QCloseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10closeEventEP11QCloseEvent(
    QWindow *self,
    QCloseEvent *a0) {
  self->closeEvent(a0);
}

//  bool QWindow::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QWindow5eventEP6QEvent(QWindow *self, QEvent *a0) {
  return self->event(a0);
}

//  void QWindow::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow13keyPressEventEP9QKeyEvent(
    QWindow *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QWindow::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15keyReleaseEventEP9QKeyEvent(
    QWindow *self,
    QKeyEvent *a0) {
  self->keyReleaseEvent(a0);
}

//  void QWindow::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow15mousePressEventEP11QMouseEvent(
    QWindow *self,
    QMouseEvent *a0) {
  self->mousePressEvent(a0);
}

//  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow17mouseReleaseEventEP11QMouseEvent(
    QWindow *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent(
    QWindow *self,
    QMouseEvent *a0) {
  self->mouseDoubleClickEvent(a0);
}

//  void QWindow::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow14mouseMoveEventEP11QMouseEvent(
    QWindow *self,
    QMouseEvent *a0) {
  self->mouseMoveEvent(a0);
}

//  void QWindow::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10wheelEventEP11QWheelEvent(
    QWindow *self,
    QWheelEvent *a0) {
  self->wheelEvent(a0);
}

//  void QWindow::touchEvent(QTouchEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow10touchEventEP11QTouchEvent(
    QWindow *self,
    QTouchEvent *a0) {
  self->touchEvent(a0);
}

//  void QWindow::tabletEvent(QTabletEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QWindow11tabletEventEP12QTabletEvent(
    QWindow *self,
    QTabletEvent *a0) {
  self->tabletEvent(a0);
}

//  QWindow as the QSurface it is built on
extern "C" Q_DECL_EXPORT
QSurface *ritual_cast_QWindow_QSurface(QWindow *self) {
  return static_cast<QSurface *>(self);
}

//  a Python function taken by a CuteQWindow, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindow(QWindow *self, const char *key, void *call) {
  return static_cast<CuteQWindow *>(self)->take(key, call);
}

//  SurfaceType QWindow::surfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_own_ZNK7QWindow11surfaceTypeEv(
    const QWindow *self) {
  return self->QWindow::surfaceType();
}

//  QSurfaceFormat QWindow::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_own_ZNK7QWindow6formatEv(const QWindow *self) {
  return new QSurfaceFormat(self->QWindow::format());
}

//  QSize QWindow::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK7QWindow4sizeEv(const QWindow *self) {
  return new QSize(self->QWindow::size());
}

//  QAccessibleInterface *QWindow::accessibleRoot() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK7QWindow14accessibleRootEv(
    const QWindow *self) {
  return self->QWindow::accessibleRoot();
}

//  QObject *QWindow::focusObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK7QWindow11focusObjectEv(const QWindow *self) {
  return self->QWindow::focusObject();
}

//  void QWindow::exposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow11exposeEventEP12QExposeEvent(
    QWindow *self,
    QExposeEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::exposeEvent(a0);
}

//  void QWindow::resizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow11resizeEventEP12QResizeEvent(
    QWindow *self,
    QResizeEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::resizeEvent(a0);
}

//  void QWindow::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow10paintEventEP11QPaintEvent(
    QWindow *self,
    QPaintEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::paintEvent(a0);
}

//  void QWindow::moveEvent(QMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow9moveEventEP10QMoveEvent(
    QWindow *self,
    QMoveEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::moveEvent(a0);
}

//  void QWindow::focusInEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow12focusInEventEP11QFocusEvent(
    QWindow *self,
    QFocusEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::focusInEvent(a0);
}

//  void QWindow::focusOutEvent(QFocusEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow13focusOutEventEP11QFocusEvent(
    QWindow *self,
    QFocusEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::focusOutEvent(a0);
}

//  void QWindow::showEvent(QShowEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow9showEventEP10QShowEvent(
    QWindow *self,
    QShowEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::showEvent(a0);
}

//  void QWindow::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow9hideEventEP10QHideEvent(
    QWindow *self,
    QHideEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::hideEvent(a0);
}

//  void QWindow::closeEvent(QCloseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow10closeEventEP11QCloseEvent(
    QWindow *self,
    QCloseEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::closeEvent(a0);
}

//  bool QWindow::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QWindow5eventEP6QEvent(QWindow *self, QEvent *a0) {
  return static_cast<OwnQWindow *>(self)->OwnQWindow::event(a0);
}

//  void QWindow::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow13keyPressEventEP9QKeyEvent(
    QWindow *self,
    QKeyEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::keyPressEvent(a0);
}

//  void QWindow::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow15keyReleaseEventEP9QKeyEvent(
    QWindow *self,
    QKeyEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::keyReleaseEvent(a0);
}

//  void QWindow::mousePressEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow15mousePressEventEP11QMouseEvent(
    QWindow *self,
    QMouseEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::mousePressEvent(a0);
}

//  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow17mouseReleaseEventEP11QMouseEvent(
    QWindow *self,
    QMouseEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::mouseReleaseEvent(a0);
}

//  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent(
    QWindow *self,
    QMouseEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::mouseDoubleClickEvent(a0);
}

//  void QWindow::mouseMoveEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow14mouseMoveEventEP11QMouseEvent(
    QWindow *self,
    QMouseEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::mouseMoveEvent(a0);
}

//  void QWindow::wheelEvent(QWheelEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow10wheelEventEP11QWheelEvent(
    QWindow *self,
    QWheelEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::wheelEvent(a0);
}

//  void QWindow::touchEvent(QTouchEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow10touchEventEP11QTouchEvent(
    QWindow *self,
    QTouchEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::touchEvent(a0);
}

//  void QWindow::tabletEvent(QTabletEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QWindow11tabletEventEP12QTabletEvent(
    QWindow *self,
    QTabletEvent *a0) {
  static_cast<OwnQWindow *>(self)->OwnQWindow::tabletEvent(a0);
}

//  QList<QWindow *>::QList()
extern "C" Q_DECL_EXPORT
QList<QWindow *> *ritual_list_make_QWindow_ptr() {
  return new QList<QWindow *>();
}

//  void QList<QWindow *>::append(const QWindow * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWindow_ptr(QList<QWindow *> *self, QWindow *element) {
  self->append(element);
}

//  qsizetype QList<QWindow *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWindow_ptr(const QList<QWindow *> *self) {
  return self->size();
}

//  const QWindow * &QList<QWindow *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWindow *ritual_list_at_QWindow_ptr(
    const QList<QWindow *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QWindow *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWindow_ptr(QList<QWindow *> *self) {
  delete self;
}
