//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformscreen.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformscreen.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpixmap.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolorspace.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtGui/qwindow.h>
#include <QtCore/qstring.h>
#include <QtGui/qtransform.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformScreen that Python can take functions over in. Every QPlatformScreen
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlatformScreenCall0)(const void *, int *);
typedef const QPixmap * (*CuteQPlatformScreenCall1)(const void *, WId, int, int, int, int, int *);
typedef const QRect * (*CuteQPlatformScreenCall2)(const void *, int *);
typedef const QRect * (*CuteQPlatformScreenCall3)(const void *, int *);
typedef int (*CuteQPlatformScreenCall4)(const void *, int *);
typedef int (*CuteQPlatformScreenCall5)(const void *, int *);
typedef const QColorSpace * (*CuteQPlatformScreenCall6)(const void *, int *);
typedef const QSizeF * (*CuteQPlatformScreenCall7)(const void *, int *);
typedef qreal (*CuteQPlatformScreenCall8)(const void *, int *);
typedef qreal (*CuteQPlatformScreenCall9)(const void *, int *);
typedef int (*CuteQPlatformScreenCall10)(const void *, int *);
typedef int (*CuteQPlatformScreenCall11)(const void *, int *);
typedef void * (*CuteQPlatformScreenCall12)(const void *, const QPoint *, int *);
typedef QString * (*CuteQPlatformScreenCall13)(const void *, int *);
typedef QString * (*CuteQPlatformScreenCall14)(const void *, int *);
typedef QString * (*CuteQPlatformScreenCall15)(const void *, int *);
typedef QString * (*CuteQPlatformScreenCall16)(const void *, int *);
typedef void * (*CuteQPlatformScreenCall17)(const void *, int *);
typedef int (*CuteQPlatformScreenCall18)(const void *, int *);
typedef int (*CuteQPlatformScreenCall19)(const void *, int *);
typedef void (*CuteQPlatformScreenCall20)(const void *, int, int *);
typedef int (*CuteQPlatformScreenCall21)(const void *, int *);
typedef int (*CuteQPlatformScreenCall22)(const void *, int *);
class CuteQPlatformScreen : public QPlatformScreen {
public:
  using QPlatformScreen::QPlatformScreen;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QPlatformScreen13isPlaceholderEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen10grabWindowEyiiii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen8geometryEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen17availableGeometryEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen5depthEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen6formatEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen10colorSpaceEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen12physicalSizeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen16devicePixelRatioEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen11refreshRateEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen17nativeOrientationEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen11orientationEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen10topLevelAtERK6QPoint")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen4nameEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen12manufacturerEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen5modelEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen12serialNumberEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen6cursorEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen28subpixelAntialiasingTypeHintEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen10powerStateEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformScreen13setPowerStateENS_10PowerStateE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen11currentModeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformScreen13preferredModeEv")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

  //  bool QPlatformScreen::isPlaceholder() const
  bool isPlaceholder() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformScreenCall0 call = reinterpret_cast<CuteQPlatformScreenCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformScreen::isPlaceholder();
  }

  //  QPixmap QPlatformScreen::grabWindow(WId window, int x, int y, int
  //      width, int height) const
  QPixmap grabWindow(
      WId window,
      int x,
      int y,
      int width,
      int height) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformScreenCall1 call = reinterpret_cast<CuteQPlatformScreenCall1>(taken[1]);
      const QPixmap * given = call(this, window, x, y, width, height, &handled);
      if (handled && given) return *given;
    }
    return QPlatformScreen::grabWindow(window, x, y, width, height);
  }

  //  QRect QPlatformScreen::geometry() const
  QRect geometry() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformScreenCall2 call = reinterpret_cast<CuteQPlatformScreenCall2>(taken[2]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QRect QPlatformScreen::availableGeometry() const
  QRect availableGeometry() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformScreenCall3 call = reinterpret_cast<CuteQPlatformScreenCall3>(taken[3]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformScreen::availableGeometry();
  }

  //  int QPlatformScreen::depth() const
  int depth() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformScreenCall4 call = reinterpret_cast<CuteQPlatformScreenCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QImage::Format QPlatformScreen::format() const
  QImage::Format format() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformScreenCall5 call = reinterpret_cast<CuteQPlatformScreenCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QImage::Format>(given);
    }
    return {};
  }

  //  QColorSpace QPlatformScreen::colorSpace() const
  QColorSpace colorSpace() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformScreenCall6 call = reinterpret_cast<CuteQPlatformScreenCall6>(taken[6]);
      const QColorSpace * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformScreen::colorSpace();
  }

  //  QSizeF QPlatformScreen::physicalSize() const
  QSizeF physicalSize() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformScreenCall7 call = reinterpret_cast<CuteQPlatformScreenCall7>(taken[7]);
      const QSizeF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformScreen::physicalSize();
  }

  //  qreal QPlatformScreen::devicePixelRatio() const
  qreal devicePixelRatio() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformScreenCall8 call = reinterpret_cast<CuteQPlatformScreenCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformScreen::devicePixelRatio();
  }

  //  qreal QPlatformScreen::refreshRate() const
  qreal refreshRate() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformScreenCall9 call = reinterpret_cast<CuteQPlatformScreenCall9>(taken[9]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformScreen::refreshRate();
  }

  //  Qt::ScreenOrientation QPlatformScreen::nativeOrientation() const
  Qt::ScreenOrientation nativeOrientation() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformScreenCall10 call = reinterpret_cast<CuteQPlatformScreenCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ScreenOrientation>(given);
    }
    return QPlatformScreen::nativeOrientation();
  }

  //  Qt::ScreenOrientation QPlatformScreen::orientation() const
  Qt::ScreenOrientation orientation() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformScreenCall11 call = reinterpret_cast<CuteQPlatformScreenCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::ScreenOrientation>(given);
    }
    return QPlatformScreen::orientation();
  }

  //  QWindow *QPlatformScreen::topLevelAt(const QPoint &point) const
  QWindow *topLevelAt(const QPoint &point) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformScreenCall12 call = reinterpret_cast<CuteQPlatformScreenCall12>(taken[12]);
      void * given = call(this, &point, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QPlatformScreen::topLevelAt(point);
  }

  //  QString QPlatformScreen::name() const
  QString name() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformScreenCall13 call = reinterpret_cast<CuteQPlatformScreenCall13>(taken[13]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformScreen::name();
  }

  //  QString QPlatformScreen::manufacturer() const
  QString manufacturer() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformScreenCall14 call = reinterpret_cast<CuteQPlatformScreenCall14>(taken[14]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformScreen::manufacturer();
  }

  //  QString QPlatformScreen::model() const
  QString model() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformScreenCall15 call = reinterpret_cast<CuteQPlatformScreenCall15>(taken[15]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformScreen::model();
  }

  //  QString QPlatformScreen::serialNumber() const
  QString serialNumber() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformScreenCall16 call = reinterpret_cast<CuteQPlatformScreenCall16>(taken[16]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformScreen::serialNumber();
  }

  //  QPlatformCursor *QPlatformScreen::cursor() const
  QPlatformCursor *cursor() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformScreenCall17 call = reinterpret_cast<CuteQPlatformScreenCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformCursor *>(given);
    }
    return QPlatformScreen::cursor();
  }

  //  SubpixelAntialiasingType
  //      QPlatformScreen::subpixelAntialiasingTypeHint() const
  QPlatformScreen::SubpixelAntialiasingType subpixelAntialiasingTypeHint() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformScreenCall18 call = reinterpret_cast<CuteQPlatformScreenCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlatformScreen::SubpixelAntialiasingType>(given);
    }
    return QPlatformScreen::subpixelAntialiasingTypeHint();
  }

  //  PowerState QPlatformScreen::powerState() const
  QPlatformScreen::PowerState powerState() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformScreenCall19 call = reinterpret_cast<CuteQPlatformScreenCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlatformScreen::PowerState>(given);
    }
    return QPlatformScreen::powerState();
  }

  //  void QPlatformScreen::setPowerState(PowerState state)
  void setPowerState(QPlatformScreen::PowerState state) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformScreenCall20 call = reinterpret_cast<CuteQPlatformScreenCall20>(taken[20]);
      call(this, static_cast<int>(state), &handled);
      if (handled) return;
    }
    QPlatformScreen::setPowerState(state);
  }

  //  int QPlatformScreen::currentMode() const
  int currentMode() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformScreenCall21 call = reinterpret_cast<CuteQPlatformScreenCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformScreen::currentMode();
  }

  //  int QPlatformScreen::preferredMode() const
  int preferredMode() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQPlatformScreenCall22 call = reinterpret_cast<CuteQPlatformScreenCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformScreen::preferredMode();
  }
};

//  QPlatformScreenPrivate *QPlatformScreen::d_func()
extern "C" Q_DECL_EXPORT
QPlatformScreenPrivate *ritual_ZN15QPlatformScreen6d_funcEv(
    QPlatformScreen *self) {
  return self->d_func();
}

//  const QPlatformScreenPrivate *QPlatformScreen::d_func() const
extern "C" Q_DECL_EXPORT
const QPlatformScreenPrivate *ritual_ZNK15QPlatformScreen6d_funcEv(
    const QPlatformScreen *self) {
  return self->d_func();
}

//  QPlatformScreen::~QPlatformScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformScreenD1Ev(QPlatformScreen *self) {
  delete self;
}

//  bool QPlatformScreen::isPlaceholder() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformScreen13isPlaceholderEv(
    const QPlatformScreen *self) {
  return self->isPlaceholder();
}

//  QPixmap QPlatformScreen::grabWindow(WId window, int x, int y, int width,
//      int height) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK15QPlatformScreen10grabWindowEyiiii(
    const QPlatformScreen *self,
    WId window,
    int x,
    int y,
    int width,
    int height) {
  return new QPixmap(self->grabWindow(window, x, y, width, height));
}

//  QRect QPlatformScreen::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QPlatformScreen8geometryEv(const QPlatformScreen *self) {
  return new QRect(self->geometry());
}

//  QRect QPlatformScreen::availableGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QPlatformScreen17availableGeometryEv(
    const QPlatformScreen *self) {
  return new QRect(self->availableGeometry());
}

//  int QPlatformScreen::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformScreen5depthEv(const QPlatformScreen *self) {
  return self->depth();
}

//  QImage::Format QPlatformScreen::format() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZNK15QPlatformScreen6formatEv(
    const QPlatformScreen *self) {
  return self->format();
}

//  QColorSpace QPlatformScreen::colorSpace() const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZNK15QPlatformScreen10colorSpaceEv(
    const QPlatformScreen *self) {
  return new QColorSpace(self->colorSpace());
}

//  QSizeF QPlatformScreen::physicalSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK15QPlatformScreen12physicalSizeEv(
    const QPlatformScreen *self) {
  return new QSizeF(self->physicalSize());
}

//  qreal QPlatformScreen::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QPlatformScreen16devicePixelRatioEv(
    const QPlatformScreen *self) {
  return self->devicePixelRatio();
}

//  qreal QPlatformScreen::refreshRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QPlatformScreen11refreshRateEv(
    const QPlatformScreen *self) {
  return self->refreshRate();
}

//  Qt::ScreenOrientation QPlatformScreen::nativeOrientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK15QPlatformScreen17nativeOrientationEv(
    const QPlatformScreen *self) {
  return self->nativeOrientation();
}

//  Qt::ScreenOrientation QPlatformScreen::orientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK15QPlatformScreen11orientationEv(
    const QPlatformScreen *self) {
  return self->orientation();
}

//  QWindow *QPlatformScreen::topLevelAt(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK15QPlatformScreen10topLevelAtERK6QPoint(
    const QPlatformScreen *self,
    const QPoint *point) {
  return self->topLevelAt(*point);
}

//  QWindowList QPlatformScreen::windows() const
extern "C" Q_DECL_EXPORT
QList<QWindow *> *ritual_ZNK15QPlatformScreen7windowsEv(
    const QPlatformScreen *self) {
  return new QList<QWindow *>(self->windows());
}

//  QList<QPlatformScreen *> QPlatformScreen::virtualSiblings() const
extern "C" Q_DECL_EXPORT
QList<QPlatformScreen *> *ritual_ZNK15QPlatformScreen15virtualSiblingsEv(
    const QPlatformScreen *self) {
  return new QList<QPlatformScreen *>(self->virtualSiblings());
}

//  const QPlatformScreen *QPlatformScreen::screenForPosition(const QPoint
//      &point) const
extern "C" Q_DECL_EXPORT
const QPlatformScreen *ritual_ZNK15QPlatformScreen17screenForPositionERK6QPoint(
    const QPlatformScreen *self,
    const QPoint *point) {
  return self->screenForPosition(*point);
}

//  QScreen *QPlatformScreen::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK15QPlatformScreen6screenEv(const QPlatformScreen *self) {
  return self->screen();
}

//  QPlatformScreen *QPlatformScreen::platformScreenForWindow(const QWindow
//      *window)
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_ZN15QPlatformScreen23platformScreenForWindowEPK7QWindow(
    const QWindow *window) {
  return QPlatformScreen::platformScreenForWindow(window);
}

//  QString QPlatformScreen::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QPlatformScreen4nameEv(const QPlatformScreen *self) {
  return new QString(self->name());
}

//  QString QPlatformScreen::manufacturer() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QPlatformScreen12manufacturerEv(
    const QPlatformScreen *self) {
  return new QString(self->manufacturer());
}

//  QString QPlatformScreen::model() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QPlatformScreen5modelEv(const QPlatformScreen *self) {
  return new QString(self->model());
}

//  QString QPlatformScreen::serialNumber() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QPlatformScreen12serialNumberEv(
    const QPlatformScreen *self) {
  return new QString(self->serialNumber());
}

//  QPlatformCursor *QPlatformScreen::cursor() const
extern "C" Q_DECL_EXPORT
QPlatformCursor *ritual_ZNK15QPlatformScreen6cursorEv(
    const QPlatformScreen *self) {
  return self->cursor();
}

//  SubpixelAntialiasingType QPlatformScreen::subpixelAntialiasingTypeHint()
//      const
extern "C" Q_DECL_EXPORT
QPlatformScreen::SubpixelAntialiasingType ritual_ZNK15QPlatformScreen28subpixelAntialiasingTypeHintEv(
    const QPlatformScreen *self) {
  return self->subpixelAntialiasingTypeHint();
}

//  PowerState QPlatformScreen::powerState() const
extern "C" Q_DECL_EXPORT
QPlatformScreen::PowerState ritual_ZNK15QPlatformScreen10powerStateEv(
    const QPlatformScreen *self) {
  return self->powerState();
}

//  void QPlatformScreen::setPowerState(PowerState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformScreen13setPowerStateENS_10PowerStateE(
    QPlatformScreen *self,
    QPlatformScreen::PowerState state) {
  self->setPowerState(state);
}

//  int QPlatformScreen::currentMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformScreen11currentModeEv(const QPlatformScreen *self) {
  return self->currentMode();
}

//  int QPlatformScreen::preferredMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPlatformScreen13preferredModeEv(
    const QPlatformScreen *self) {
  return self->preferredMode();
}

//  int QPlatformScreen::angleBetween(Qt::ScreenOrientation a,
//      Qt::ScreenOrientation b)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QPlatformScreen12angleBetweenEN2Qt17ScreenOrientationES1_(
    Qt::ScreenOrientation a,
    Qt::ScreenOrientation b) {
  return QPlatformScreen::angleBetween(a, b);
}

//  QTransform QPlatformScreen::transformBetween(Qt::ScreenOrientation a,
//      Qt::ScreenOrientation b, const QRect &target)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN15QPlatformScreen16transformBetweenEN2Qt17ScreenOrientationES1_RK5QRect(
    Qt::ScreenOrientation a,
    Qt::ScreenOrientation b,
    const QRect *target) {
  return new QTransform(QPlatformScreen::transformBetween(a, b, *target));
}

//  QRect QPlatformScreen::mapBetween(Qt::ScreenOrientation a,
//      Qt::ScreenOrientation b, const QRect &rect)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN15QPlatformScreen10mapBetweenEN2Qt17ScreenOrientationES1_RK5QRect(
    Qt::ScreenOrientation a,
    Qt::ScreenOrientation b,
    const QRect *rect) {
  return new QRect(QPlatformScreen::mapBetween(a, b, *rect));
}

//  void QPlatformScreen::resizeMaximizedWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformScreen22resizeMaximizedWindowsEv(
    QPlatformScreen *self) {
  self->resizeMaximizedWindows();
}

//  a Python function taken by a CuteQPlatformScreen, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformScreen(
    QPlatformScreen *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformScreen *>(self)->take(key, call);
}

//  bool QPlatformScreen::isPlaceholder() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformScreen13isPlaceholderEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::isPlaceholder();
}

//  QPixmap QPlatformScreen::grabWindow(WId window, int x, int y, int width,
//      int height) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_own_ZNK15QPlatformScreen10grabWindowEyiiii(
    const QPlatformScreen *self,
    WId window,
    int x,
    int y,
    int width,
    int height) {
  return new QPixmap(
      self->QPlatformScreen::grabWindow(
          window,
          x,
          y,
          width,
          height));
}

//  QRect QPlatformScreen::availableGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK15QPlatformScreen17availableGeometryEv(
    const QPlatformScreen *self) {
  return new QRect(self->QPlatformScreen::availableGeometry());
}

//  QColorSpace QPlatformScreen::colorSpace() const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_own_ZNK15QPlatformScreen10colorSpaceEv(
    const QPlatformScreen *self) {
  return new QColorSpace(self->QPlatformScreen::colorSpace());
}

//  QSizeF QPlatformScreen::physicalSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK15QPlatformScreen12physicalSizeEv(
    const QPlatformScreen *self) {
  return new QSizeF(self->QPlatformScreen::physicalSize());
}

//  qreal QPlatformScreen::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QPlatformScreen16devicePixelRatioEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::devicePixelRatio();
}

//  qreal QPlatformScreen::refreshRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QPlatformScreen11refreshRateEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::refreshRate();
}

//  Qt::ScreenOrientation QPlatformScreen::nativeOrientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_own_ZNK15QPlatformScreen17nativeOrientationEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::nativeOrientation();
}

//  Qt::ScreenOrientation QPlatformScreen::orientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_own_ZNK15QPlatformScreen11orientationEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::orientation();
}

//  QWindow *QPlatformScreen::topLevelAt(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZNK15QPlatformScreen10topLevelAtERK6QPoint(
    const QPlatformScreen *self,
    const QPoint *point) {
  return self->QPlatformScreen::topLevelAt(*point);
}

//  QString QPlatformScreen::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QPlatformScreen4nameEv(
    const QPlatformScreen *self) {
  return new QString(self->QPlatformScreen::name());
}

//  QString QPlatformScreen::manufacturer() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QPlatformScreen12manufacturerEv(
    const QPlatformScreen *self) {
  return new QString(self->QPlatformScreen::manufacturer());
}

//  QString QPlatformScreen::model() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QPlatformScreen5modelEv(
    const QPlatformScreen *self) {
  return new QString(self->QPlatformScreen::model());
}

//  QString QPlatformScreen::serialNumber() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QPlatformScreen12serialNumberEv(
    const QPlatformScreen *self) {
  return new QString(self->QPlatformScreen::serialNumber());
}

//  QPlatformCursor *QPlatformScreen::cursor() const
extern "C" Q_DECL_EXPORT
QPlatformCursor *ritual_own_ZNK15QPlatformScreen6cursorEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::cursor();
}

//  SubpixelAntialiasingType QPlatformScreen::subpixelAntialiasingTypeHint()
//      const
extern "C" Q_DECL_EXPORT
QPlatformScreen::SubpixelAntialiasingType ritual_own_ZNK15QPlatformScreen28subpixelAntialiasingTypeHintEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::subpixelAntialiasingTypeHint();
}

//  PowerState QPlatformScreen::powerState() const
extern "C" Q_DECL_EXPORT
QPlatformScreen::PowerState ritual_own_ZNK15QPlatformScreen10powerStateEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::powerState();
}

//  void QPlatformScreen::setPowerState(PowerState state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformScreen13setPowerStateENS_10PowerStateE(
    QPlatformScreen *self,
    QPlatformScreen::PowerState state) {
  self->QPlatformScreen::setPowerState(state);
}

//  int QPlatformScreen::currentMode() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QPlatformScreen11currentModeEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::currentMode();
}

//  int QPlatformScreen::preferredMode() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QPlatformScreen13preferredModeEv(
    const QPlatformScreen *self) {
  return self->QPlatformScreen::preferredMode();
}

//  QList<QPlatformScreen *>::QList()
extern "C" Q_DECL_EXPORT
QList<QPlatformScreen *> *ritual_list_make_QPlatformScreen_ptr() {
  return new QList<QPlatformScreen *>();
}

//  void QList<QPlatformScreen *>::append(const QPlatformScreen * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPlatformScreen_ptr(
    QList<QPlatformScreen *> *self,
    QPlatformScreen *element) {
  self->append(element);
}

//  qsizetype QList<QPlatformScreen *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPlatformScreen_ptr(
    const QList<QPlatformScreen *> *self) {
  return self->size();
}

//  const QPlatformScreen * &QList<QPlatformScreen *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_list_at_QPlatformScreen_ptr(
    const QList<QPlatformScreen *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QPlatformScreen *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPlatformScreen_ptr(QList<QPlatformScreen *> *self) {
  delete self;
}
