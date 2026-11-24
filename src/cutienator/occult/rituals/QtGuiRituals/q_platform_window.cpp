//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformwindow.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformwindow.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qpoint.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QPlatformWindow that Python can take functions over in. Every QPlatformWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformWindowCall0)(const void *, int *);
typedef void * (*CuteQPlatformWindowCall1)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQPlatformWindowCall2)(const void *, int *);
typedef void (*CuteQPlatformWindowCall3)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQPlatformWindowCall4)(const void *, int *);
typedef const QRect * (*CuteQPlatformWindowCall5)(const void *, int *);
typedef const QMargins * (*CuteQPlatformWindowCall6)(const void *, int *);
typedef const QMargins * (*CuteQPlatformWindowCall7)(const void *, int *);
typedef void (*CuteQPlatformWindowCall8)(const void *, bool, int *);
typedef void (*CuteQPlatformWindowCall9)(const void *, int, int *);
typedef void (*CuteQPlatformWindowCall10)(const void *, int, int *);
typedef WId (*CuteQPlatformWindowCall11)(const void *, int *);
typedef void (*CuteQPlatformWindowCall12)(const void *, const QPlatformWindow *, int *);
typedef void (*CuteQPlatformWindowCall13)(const void *, const QString *, int *);
typedef QString * (*CuteQPlatformWindowCall14)(const void *, int *);
typedef void (*CuteQPlatformWindowCall15)(const void *, const QString *, int *);
typedef void (*CuteQPlatformWindowCall16)(const void *, const QIcon *, int *);
typedef bool (*CuteQPlatformWindowCall17)(const void *, int *);
typedef void (*CuteQPlatformWindowCall18)(const void *, int *);
typedef void (*CuteQPlatformWindowCall19)(const void *, int *);
typedef bool (*CuteQPlatformWindowCall20)(const void *, int *);
typedef bool (*CuteQPlatformWindowCall21)(const void *, int *);
typedef bool (*CuteQPlatformWindowCall22)(const void *, const QPlatformWindow *, int *);
typedef bool (*CuteQPlatformWindowCall23)(const void *, int *);
typedef bool (*CuteQPlatformWindowCall24)(const void *, int *);
typedef const QPoint * (*CuteQPlatformWindowCall25)(const void *, const QPoint *, int *);
typedef const QPoint * (*CuteQPlatformWindowCall26)(const void *, const QPoint *, int *);
typedef void (*CuteQPlatformWindowCall27)(const void *, int *);
typedef void (*CuteQPlatformWindowCall28)(const void *, qreal, int *);
typedef void (*CuteQPlatformWindowCall29)(const void *, const QRegion *, int *);
typedef void (*CuteQPlatformWindowCall30)(const void *, int *);
typedef void (*CuteQPlatformWindowCall31)(const void *, int, int *);
typedef qreal (*CuteQPlatformWindowCall32)(const void *, int *);
typedef bool (*CuteQPlatformWindowCall33)(const void *, bool, int *);
typedef bool (*CuteQPlatformWindowCall34)(const void *, bool, int *);
typedef bool (*CuteQPlatformWindowCall35)(const void *, bool, int *);
typedef bool (*CuteQPlatformWindowCall36)(const void *, QEvent *, int *);
typedef bool (*CuteQPlatformWindowCall37)(const void *, int, int *);
typedef bool (*CuteQPlatformWindowCall38)(const void *, int *);
typedef void (*CuteQPlatformWindowCall39)(const void *, bool, int *);
typedef bool (*CuteQPlatformWindowCall40)(const void *, int *);
typedef void (*CuteQPlatformWindowCall41)(const void *, bool, int *);
typedef bool (*CuteQPlatformWindowCall42)(const void *, int *);
typedef void (*CuteQPlatformWindowCall43)(const void *, int *);
typedef void (*CuteQPlatformWindowCall44)(const void *, int *);
typedef void (*CuteQPlatformWindowCall45)(const void *, int *);
typedef bool (*CuteQPlatformWindowCall46)(const void *, int *);
class CuteQPlatformWindow : public QPlatformWindow {
public:
  using QPlatformWindow::QPlatformWindow;
  void *taken[47] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QPlatformWindow10initializeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformSurface6screenEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformSurface6formatEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow11setGeometryERK5QRect")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow8geometryEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow14normalGeometryEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow12frameMarginsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow15safeAreaMarginsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow10setVisibleEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow14setWindowStateE6QFlagsIN2Qt11WindowStateEE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow5winIdEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow9setParentEPKS_")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow14setWindowTitleERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow11windowTitleEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow17setWindowFilePathERK7QString")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow13setWindowIconERK5QIcon")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow5closeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow5raiseEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow5lowerEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow9isExposedEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow8isActiveEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow12isAncestorOfEPKS_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow10isEmbeddedEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow15isForeignWindowEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow11mapToGlobalERK6QPoint")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow13mapFromGlobalERK6QPoint")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow18propagateSizeHintsEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow10setOpacityEd")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow7setMaskERK7QRegion")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow21requestActivateWindowEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow30handleContentOrientationChangeEN2Qt17ScreenOrientationE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow16devicePixelRatioEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow22setKeyboardGrabEnabledEb")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow19setMouseGrabEnabledEb")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow17setWindowModifiedEb")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow11windowEventEP6QEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow17startSystemResizeE6QFlagsIN2Qt4EdgeEE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow15startSystemMoveEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow26setFrameStrutEventsEnabledEb")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow23frameStrutEventsEnabledEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow13setAlertStateEb")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow12isAlertStateEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow17invalidateSurfaceEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow13requestUpdateEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QPlatformWindow20deliverUpdateRequestEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QPlatformWindow34allowsIndependentThreadedRenderingEv")) {
      taken[46] = call;
      return true;
    }
    return false;
  }

  //  void QPlatformWindow::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformWindowCall0 call = reinterpret_cast<CuteQPlatformWindowCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformWindow::initialize();
  }

  //  QPlatformScreen *QPlatformWindow::screen() const
  QPlatformScreen *screen() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformWindowCall1 call = reinterpret_cast<CuteQPlatformWindowCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformScreen *>(given);
    }
    return QPlatformWindow::screen();
  }

  //  QSurfaceFormat QPlatformWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformWindowCall2 call = reinterpret_cast<CuteQPlatformWindowCall2>(taken[2]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformWindow::format();
  }

  //  void QPlatformWindow::setGeometry(const QRect &rect)
  void setGeometry(const QRect &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformWindowCall3 call = reinterpret_cast<CuteQPlatformWindowCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QPlatformWindow::setGeometry(rect);
  }

  //  QRect QPlatformWindow::geometry() const
  QRect geometry() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformWindowCall4 call = reinterpret_cast<CuteQPlatformWindowCall4>(taken[4]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformWindow::geometry();
  }

  //  QRect QPlatformWindow::normalGeometry() const
  QRect normalGeometry() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformWindowCall5 call = reinterpret_cast<CuteQPlatformWindowCall5>(taken[5]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformWindow::normalGeometry();
  }

  //  QMargins QPlatformWindow::frameMargins() const
  QMargins frameMargins() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformWindowCall6 call = reinterpret_cast<CuteQPlatformWindowCall6>(taken[6]);
      const QMargins * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformWindow::frameMargins();
  }

  //  QMargins QPlatformWindow::safeAreaMargins() const
  QMargins safeAreaMargins() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformWindowCall7 call = reinterpret_cast<CuteQPlatformWindowCall7>(taken[7]);
      const QMargins * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformWindow::safeAreaMargins();
  }

  //  void QPlatformWindow::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformWindowCall8 call = reinterpret_cast<CuteQPlatformWindowCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QPlatformWindow::setVisible(visible);
  }

  //  void QPlatformWindow::setWindowFlags(Qt::WindowFlags flags)
  void setWindowFlags(Qt::WindowFlags flags) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformWindowCall9 call = reinterpret_cast<CuteQPlatformWindowCall9>(taken[9]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QPlatformWindow::setWindowFlags(flags);
  }

  //  void QPlatformWindow::setWindowState(Qt::WindowStates state)
  void setWindowState(Qt::WindowStates state) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformWindowCall10 call = reinterpret_cast<CuteQPlatformWindowCall10>(taken[10]);
      call(this, static_cast<int>(state.toInt()), &handled);
      if (handled) return;
    }
    QPlatformWindow::setWindowState(state);
  }

  //  WId QPlatformWindow::winId() const
  WId winId() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformWindowCall11 call = reinterpret_cast<CuteQPlatformWindowCall11>(taken[11]);
      WId given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::winId();
  }

  //  void QPlatformWindow::setParent(const QPlatformWindow *window)
  void setParent(const QPlatformWindow *window) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformWindowCall12 call = reinterpret_cast<CuteQPlatformWindowCall12>(taken[12]);
      call(this, window, &handled);
      if (handled) return;
    }
    QPlatformWindow::setParent(window);
  }

  //  void QPlatformWindow::setWindowTitle(const QString &title)
  void setWindowTitle(const QString &title) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformWindowCall13 call = reinterpret_cast<CuteQPlatformWindowCall13>(taken[13]);
      call(this, &title, &handled);
      if (handled) return;
    }
    QPlatformWindow::setWindowTitle(title);
  }

  //  QString QPlatformWindow::windowTitle() const
  QString windowTitle() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformWindowCall14 call = reinterpret_cast<CuteQPlatformWindowCall14>(taken[14]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformWindow::windowTitle();
  }

  //  void QPlatformWindow::setWindowFilePath(const QString &title)
  void setWindowFilePath(const QString &title) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformWindowCall15 call = reinterpret_cast<CuteQPlatformWindowCall15>(taken[15]);
      call(this, &title, &handled);
      if (handled) return;
    }
    QPlatformWindow::setWindowFilePath(title);
  }

  //  void QPlatformWindow::setWindowIcon(const QIcon &icon)
  void setWindowIcon(const QIcon &icon) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformWindowCall16 call = reinterpret_cast<CuteQPlatformWindowCall16>(taken[16]);
      call(this, &icon, &handled);
      if (handled) return;
    }
    QPlatformWindow::setWindowIcon(icon);
  }

  //  bool QPlatformWindow::close()
  bool close() override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformWindowCall17 call = reinterpret_cast<CuteQPlatformWindowCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::close();
  }

  //  void QPlatformWindow::raise()
  void raise() override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformWindowCall18 call = reinterpret_cast<CuteQPlatformWindowCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformWindow::raise();
  }

  //  void QPlatformWindow::lower()
  void lower() override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformWindowCall19 call = reinterpret_cast<CuteQPlatformWindowCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformWindow::lower();
  }

  //  bool QPlatformWindow::isExposed() const
  bool isExposed() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformWindowCall20 call = reinterpret_cast<CuteQPlatformWindowCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::isExposed();
  }

  //  bool QPlatformWindow::isActive() const
  bool isActive() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformWindowCall21 call = reinterpret_cast<CuteQPlatformWindowCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::isActive();
  }

  //  bool QPlatformWindow::isAncestorOf(const QPlatformWindow *child)
  //      const
  bool isAncestorOf(const QPlatformWindow *child) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQPlatformWindowCall22 call = reinterpret_cast<CuteQPlatformWindowCall22>(taken[22]);
      bool given = call(this, child, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::isAncestorOf(child);
  }

  //  bool QPlatformWindow::isEmbedded() const
  bool isEmbedded() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQPlatformWindowCall23 call = reinterpret_cast<CuteQPlatformWindowCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::isEmbedded();
  }

  //  bool QPlatformWindow::isForeignWindow() const
  bool isForeignWindow() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQPlatformWindowCall24 call = reinterpret_cast<CuteQPlatformWindowCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::isForeignWindow();
  }

  //  QPoint QPlatformWindow::mapToGlobal(const QPoint &pos) const
  QPoint mapToGlobal(const QPoint &pos) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQPlatformWindowCall25 call = reinterpret_cast<CuteQPlatformWindowCall25>(taken[25]);
      const QPoint * given = call(this, &pos, &handled);
      if (handled && given) return *given;
    }
    return QPlatformWindow::mapToGlobal(pos);
  }

  //  QPoint QPlatformWindow::mapFromGlobal(const QPoint &pos) const
  QPoint mapFromGlobal(const QPoint &pos) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQPlatformWindowCall26 call = reinterpret_cast<CuteQPlatformWindowCall26>(taken[26]);
      const QPoint * given = call(this, &pos, &handled);
      if (handled && given) return *given;
    }
    return QPlatformWindow::mapFromGlobal(pos);
  }

  //  void QPlatformWindow::propagateSizeHints()
  void propagateSizeHints() override {
    if (taken[27]) {
      int handled = 0;
      CuteQPlatformWindowCall27 call = reinterpret_cast<CuteQPlatformWindowCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformWindow::propagateSizeHints();
  }

  //  void QPlatformWindow::setOpacity(qreal level)
  void setOpacity(qreal level) override {
    if (taken[28]) {
      int handled = 0;
      CuteQPlatformWindowCall28 call = reinterpret_cast<CuteQPlatformWindowCall28>(taken[28]);
      call(this, level, &handled);
      if (handled) return;
    }
    QPlatformWindow::setOpacity(level);
  }

  //  void QPlatformWindow::setMask(const QRegion &region)
  void setMask(const QRegion &region) override {
    if (taken[29]) {
      int handled = 0;
      CuteQPlatformWindowCall29 call = reinterpret_cast<CuteQPlatformWindowCall29>(taken[29]);
      call(this, &region, &handled);
      if (handled) return;
    }
    QPlatformWindow::setMask(region);
  }

  //  void QPlatformWindow::requestActivateWindow()
  void requestActivateWindow() override {
    if (taken[30]) {
      int handled = 0;
      CuteQPlatformWindowCall30 call = reinterpret_cast<CuteQPlatformWindowCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformWindow::requestActivateWindow();
  }

  //  void
  //      QPlatformWindow::handleContentOrientationChange(Qt::ScreenOrienta
  //      tion orientation)
  void handleContentOrientationChange(
      Qt::ScreenOrientation orientation) override {
    if (taken[31]) {
      int handled = 0;
      CuteQPlatformWindowCall31 call = reinterpret_cast<CuteQPlatformWindowCall31>(taken[31]);
      call(this, static_cast<int>(orientation), &handled);
      if (handled) return;
    }
    QPlatformWindow::handleContentOrientationChange(orientation);
  }

  //  qreal QPlatformWindow::devicePixelRatio() const
  qreal devicePixelRatio() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQPlatformWindowCall32 call = reinterpret_cast<CuteQPlatformWindowCall32>(taken[32]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::devicePixelRatio();
  }

  //  bool QPlatformWindow::setKeyboardGrabEnabled(bool grab)
  bool setKeyboardGrabEnabled(bool grab) override {
    if (taken[33]) {
      int handled = 0;
      CuteQPlatformWindowCall33 call = reinterpret_cast<CuteQPlatformWindowCall33>(taken[33]);
      bool given = call(this, grab, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::setKeyboardGrabEnabled(grab);
  }

  //  bool QPlatformWindow::setMouseGrabEnabled(bool grab)
  bool setMouseGrabEnabled(bool grab) override {
    if (taken[34]) {
      int handled = 0;
      CuteQPlatformWindowCall34 call = reinterpret_cast<CuteQPlatformWindowCall34>(taken[34]);
      bool given = call(this, grab, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::setMouseGrabEnabled(grab);
  }

  //  bool QPlatformWindow::setWindowModified(bool modified)
  bool setWindowModified(bool modified) override {
    if (taken[35]) {
      int handled = 0;
      CuteQPlatformWindowCall35 call = reinterpret_cast<CuteQPlatformWindowCall35>(taken[35]);
      bool given = call(this, modified, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::setWindowModified(modified);
  }

  //  bool QPlatformWindow::windowEvent(QEvent *event)
  bool windowEvent(QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQPlatformWindowCall36 call = reinterpret_cast<CuteQPlatformWindowCall36>(taken[36]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::windowEvent(event);
  }

  //  bool QPlatformWindow::startSystemResize(Qt::Edges edges)
  bool startSystemResize(Qt::Edges edges) override {
    if (taken[37]) {
      int handled = 0;
      CuteQPlatformWindowCall37 call = reinterpret_cast<CuteQPlatformWindowCall37>(taken[37]);
      bool given = call(this, static_cast<int>(edges.toInt()), &handled);
      if (handled) return given;
    }
    return QPlatformWindow::startSystemResize(edges);
  }

  //  bool QPlatformWindow::startSystemMove()
  bool startSystemMove() override {
    if (taken[38]) {
      int handled = 0;
      CuteQPlatformWindowCall38 call = reinterpret_cast<CuteQPlatformWindowCall38>(taken[38]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::startSystemMove();
  }

  //  void QPlatformWindow::setFrameStrutEventsEnabled(bool enabled)
  void setFrameStrutEventsEnabled(bool enabled) override {
    if (taken[39]) {
      int handled = 0;
      CuteQPlatformWindowCall39 call = reinterpret_cast<CuteQPlatformWindowCall39>(taken[39]);
      call(this, enabled, &handled);
      if (handled) return;
    }
    QPlatformWindow::setFrameStrutEventsEnabled(enabled);
  }

  //  bool QPlatformWindow::frameStrutEventsEnabled() const
  bool frameStrutEventsEnabled() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQPlatformWindowCall40 call = reinterpret_cast<CuteQPlatformWindowCall40>(taken[40]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::frameStrutEventsEnabled();
  }

  //  void QPlatformWindow::setAlertState(bool enabled)
  void setAlertState(bool enabled) override {
    if (taken[41]) {
      int handled = 0;
      CuteQPlatformWindowCall41 call = reinterpret_cast<CuteQPlatformWindowCall41>(taken[41]);
      call(this, enabled, &handled);
      if (handled) return;
    }
    QPlatformWindow::setAlertState(enabled);
  }

  //  bool QPlatformWindow::isAlertState() const
  bool isAlertState() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQPlatformWindowCall42 call = reinterpret_cast<CuteQPlatformWindowCall42>(taken[42]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::isAlertState();
  }

  //  void QPlatformWindow::invalidateSurface()
  void invalidateSurface() override {
    if (taken[43]) {
      int handled = 0;
      CuteQPlatformWindowCall43 call = reinterpret_cast<CuteQPlatformWindowCall43>(taken[43]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformWindow::invalidateSurface();
  }

  //  void QPlatformWindow::requestUpdate()
  void requestUpdate() override {
    if (taken[44]) {
      int handled = 0;
      CuteQPlatformWindowCall44 call = reinterpret_cast<CuteQPlatformWindowCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformWindow::requestUpdate();
  }

  //  void QPlatformWindow::deliverUpdateRequest()
  void deliverUpdateRequest() override {
    if (taken[45]) {
      int handled = 0;
      CuteQPlatformWindowCall45 call = reinterpret_cast<CuteQPlatformWindowCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformWindow::deliverUpdateRequest();
  }

  //  bool QPlatformWindow::allowsIndependentThreadedRendering() const
  bool allowsIndependentThreadedRendering() const override {
    if (taken[46]) {
      int handled = 0;
      CuteQPlatformWindowCall46 call = reinterpret_cast<CuteQPlatformWindowCall46>(taken[46]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformWindow::allowsIndependentThreadedRendering();
  }
};

//  QPlatformWindowPrivate *QPlatformWindow::d_func()
extern "C" Q_DECL_EXPORT
QPlatformWindowPrivate *ritual_ZN15QPlatformWindow6d_funcEv(
    QPlatformWindow *self) {
  return self->d_func();
}

//  const QPlatformWindowPrivate *QPlatformWindow::d_func() const
extern "C" Q_DECL_EXPORT
const QPlatformWindowPrivate *ritual_ZNK15QPlatformWindow6d_funcEv(
    const QPlatformWindow *self) {
  return self->d_func();
}

//  QPlatformWindow::QPlatformWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
QPlatformWindow *ritual_ZN15QPlatformWindowC1EP7QWindow(QWindow *window) {
  return new CuteQPlatformWindow(window);
}

//  QPlatformWindow::~QPlatformWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindowD1Ev(QPlatformWindow *self) {
  delete self;
}

//  void QPlatformWindow::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow10initializeEv(QPlatformWindow *self) {
  self->initialize();
}

//  QWindow *QPlatformWindow::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK15QPlatformWindow6windowEv(const QPlatformWindow *self) {
  return self->window();
}

//  QPlatformWindow *QPlatformWindow::parent() const
extern "C" Q_DECL_EXPORT
QPlatformWindow *ritual_ZNK15QPlatformWindow6parentEv(
    const QPlatformWindow *self) {
  return self->parent();
}

//  QPlatformScreen *QPlatformWindow::screen() const
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_ZNK15QPlatformWindow6screenEv(
    const QPlatformWindow *self) {
  return self->screen();
}

//  QSurfaceFormat QPlatformWindow::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK15QPlatformWindow6formatEv(
    const QPlatformWindow *self) {
  return new QSurfaceFormat(self->format());
}

//  void QPlatformWindow::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow11setGeometryERK5QRect(
    QPlatformWindow *self,
    const QRect *rect) {
  self->setGeometry(*rect);
}

//  QRect QPlatformWindow::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QPlatformWindow8geometryEv(const QPlatformWindow *self) {
  return new QRect(self->geometry());
}

//  QRect QPlatformWindow::normalGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QPlatformWindow14normalGeometryEv(
    const QPlatformWindow *self) {
  return new QRect(self->normalGeometry());
}

//  QMargins QPlatformWindow::frameMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK15QPlatformWindow12frameMarginsEv(
    const QPlatformWindow *self) {
  return new QMargins(self->frameMargins());
}

//  QMargins QPlatformWindow::safeAreaMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK15QPlatformWindow15safeAreaMarginsEv(
    const QPlatformWindow *self) {
  return new QMargins(self->safeAreaMargins());
}

//  void QPlatformWindow::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow10setVisibleEb(
    QPlatformWindow *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QPlatformWindow::setWindowFlags(Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QPlatformWindow *self,
    int flags) {
  self->setWindowFlags(QFlags<Qt::WindowType>::fromInt(flags));
}

//  void QPlatformWindow::setWindowState(Qt::WindowStates state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow14setWindowStateE6QFlagsIN2Qt11WindowStateEE(
    QPlatformWindow *self,
    int state) {
  self->setWindowState(QFlags<Qt::WindowState>::fromInt(state));
}

//  WId QPlatformWindow::winId() const
extern "C" Q_DECL_EXPORT
WId ritual_ZNK15QPlatformWindow5winIdEv(const QPlatformWindow *self) {
  return self->winId();
}

//  void QPlatformWindow::setParent(const QPlatformWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow9setParentEPKS_(
    QPlatformWindow *self,
    const QPlatformWindow *window) {
  self->setParent(window);
}

//  void QPlatformWindow::setWindowTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow14setWindowTitleERK7QString(
    QPlatformWindow *self,
    const QString *title) {
  self->setWindowTitle(*title);
}

//  QString QPlatformWindow::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QPlatformWindow11windowTitleEv(
    const QPlatformWindow *self) {
  return new QString(self->windowTitle());
}

//  void QPlatformWindow::setWindowFilePath(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow17setWindowFilePathERK7QString(
    QPlatformWindow *self,
    const QString *title) {
  self->setWindowFilePath(*title);
}

//  void QPlatformWindow::setWindowIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow13setWindowIconERK5QIcon(
    QPlatformWindow *self,
    const QIcon *icon) {
  self->setWindowIcon(*icon);
}

//  bool QPlatformWindow::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformWindow5closeEv(QPlatformWindow *self) {
  return self->close();
}

//  void QPlatformWindow::raise()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow5raiseEv(QPlatformWindow *self) {
  self->raise();
}

//  void QPlatformWindow::lower()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow5lowerEv(QPlatformWindow *self) {
  self->lower();
}

//  bool QPlatformWindow::isExposed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow9isExposedEv(const QPlatformWindow *self) {
  return self->isExposed();
}

//  bool QPlatformWindow::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow8isActiveEv(const QPlatformWindow *self) {
  return self->isActive();
}

//  bool QPlatformWindow::isAncestorOf(const QPlatformWindow *child) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow12isAncestorOfEPKS_(
    const QPlatformWindow *self,
    const QPlatformWindow *child) {
  return self->isAncestorOf(child);
}

//  bool QPlatformWindow::isEmbedded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow10isEmbeddedEv(const QPlatformWindow *self) {
  return self->isEmbedded();
}

//  bool QPlatformWindow::isForeignWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow15isForeignWindowEv(
    const QPlatformWindow *self) {
  return self->isForeignWindow();
}

//  QPoint QPlatformWindow::mapToGlobal(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK15QPlatformWindow11mapToGlobalERK6QPoint(
    const QPlatformWindow *self,
    const QPoint *pos) {
  return new QPoint(self->mapToGlobal(*pos));
}

//  QPointF QPlatformWindow::mapToGlobalF(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QPlatformWindow12mapToGlobalFERK7QPointF(
    const QPlatformWindow *self,
    const QPointF *pos) {
  return new QPointF(self->mapToGlobalF(*pos));
}

//  QPoint QPlatformWindow::mapFromGlobal(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK15QPlatformWindow13mapFromGlobalERK6QPoint(
    const QPlatformWindow *self,
    const QPoint *pos) {
  return new QPoint(self->mapFromGlobal(*pos));
}

//  QPointF QPlatformWindow::mapFromGlobalF(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QPlatformWindow14mapFromGlobalFERK7QPointF(
    const QPlatformWindow *self,
    const QPointF *pos) {
  return new QPointF(self->mapFromGlobalF(*pos));
}

//  void QPlatformWindow::propagateSizeHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow18propagateSizeHintsEv(
    QPlatformWindow *self) {
  self->propagateSizeHints();
}

//  void QPlatformWindow::setOpacity(qreal level)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow10setOpacityEd(
    QPlatformWindow *self,
    qreal level) {
  self->setOpacity(level);
}

//  void QPlatformWindow::setMask(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow7setMaskERK7QRegion(
    QPlatformWindow *self,
    const QRegion *region) {
  self->setMask(*region);
}

//  void QPlatformWindow::requestActivateWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow21requestActivateWindowEv(
    QPlatformWindow *self) {
  self->requestActivateWindow();
}

//  void
//      QPlatformWindow::handleContentOrientationChange(Qt::ScreenOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow30handleContentOrientationChangeEN2Qt17ScreenOrientationE(
    QPlatformWindow *self,
    Qt::ScreenOrientation orientation) {
  self->handleContentOrientationChange(orientation);
}

//  qreal QPlatformWindow::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QPlatformWindow16devicePixelRatioEv(
    const QPlatformWindow *self) {
  return self->devicePixelRatio();
}

//  bool QPlatformWindow::setKeyboardGrabEnabled(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformWindow22setKeyboardGrabEnabledEb(
    QPlatformWindow *self,
    bool grab) {
  return self->setKeyboardGrabEnabled(grab);
}

//  bool QPlatformWindow::setMouseGrabEnabled(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformWindow19setMouseGrabEnabledEb(
    QPlatformWindow *self,
    bool grab) {
  return self->setMouseGrabEnabled(grab);
}

//  bool QPlatformWindow::setWindowModified(bool modified)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformWindow17setWindowModifiedEb(
    QPlatformWindow *self,
    bool modified) {
  return self->setWindowModified(modified);
}

//  bool QPlatformWindow::windowEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformWindow11windowEventEP6QEvent(
    QPlatformWindow *self,
    QEvent *event) {
  return self->windowEvent(event);
}

//  bool QPlatformWindow::startSystemResize(Qt::Edges edges)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformWindow17startSystemResizeE6QFlagsIN2Qt4EdgeEE(
    QPlatformWindow *self,
    int edges) {
  return self->startSystemResize(QFlags<Qt::Edge>::fromInt(edges));
}

//  bool QPlatformWindow::startSystemMove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformWindow15startSystemMoveEv(QPlatformWindow *self) {
  return self->startSystemMove();
}

//  void QPlatformWindow::setFrameStrutEventsEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow26setFrameStrutEventsEnabledEb(
    QPlatformWindow *self,
    bool enabled) {
  self->setFrameStrutEventsEnabled(enabled);
}

//  bool QPlatformWindow::frameStrutEventsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow23frameStrutEventsEnabledEv(
    const QPlatformWindow *self) {
  return self->frameStrutEventsEnabled();
}

//  void QPlatformWindow::setAlertState(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow13setAlertStateEb(
    QPlatformWindow *self,
    bool enabled) {
  self->setAlertState(enabled);
}

//  bool QPlatformWindow::isAlertState() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow12isAlertStateEv(
    const QPlatformWindow *self) {
  return self->isAlertState();
}

//  void QPlatformWindow::invalidateSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow17invalidateSurfaceEv(QPlatformWindow *self) {
  self->invalidateSurface();
}

//  void QPlatformWindow::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow13requestUpdateEv(QPlatformWindow *self) {
  self->requestUpdate();
}

//  bool QPlatformWindow::hasPendingUpdateRequest() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow23hasPendingUpdateRequestEv(
    const QPlatformWindow *self) {
  return self->hasPendingUpdateRequest();
}

//  void QPlatformWindow::deliverUpdateRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformWindow20deliverUpdateRequestEv(
    QPlatformWindow *self) {
  self->deliverUpdateRequest();
}

//  bool QPlatformWindow::allowsIndependentThreadedRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPlatformWindow34allowsIndependentThreadedRenderingEv(
    const QPlatformWindow *self) {
  return self->allowsIndependentThreadedRendering();
}

//  QSize QPlatformWindow::windowMinimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QPlatformWindow17windowMinimumSizeEv(
    const QPlatformWindow *self) {
  return new QSize(self->windowMinimumSize());
}

//  QSize QPlatformWindow::windowMaximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QPlatformWindow17windowMaximumSizeEv(
    const QPlatformWindow *self) {
  return new QSize(self->windowMaximumSize());
}

//  QSize QPlatformWindow::windowBaseSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QPlatformWindow14windowBaseSizeEv(
    const QPlatformWindow *self) {
  return new QSize(self->windowBaseSize());
}

//  QSize QPlatformWindow::windowSizeIncrement() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QPlatformWindow19windowSizeIncrementEv(
    const QPlatformWindow *self) {
  return new QSize(self->windowSizeIncrement());
}

//  QRect QPlatformWindow::windowGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QPlatformWindow14windowGeometryEv(
    const QPlatformWindow *self) {
  return new QRect(self->windowGeometry());
}

//  QRect QPlatformWindow::windowFrameGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QPlatformWindow19windowFrameGeometryEv(
    const QPlatformWindow *self) {
  return new QRect(self->windowFrameGeometry());
}

//  QRectF QPlatformWindow::windowClosestAcceptableGeometry(const QRectF
//      &nativeRect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QPlatformWindow31windowClosestAcceptableGeometryERK6QRectF(
    const QPlatformWindow *self,
    const QRectF *nativeRect) {
  return new QRectF(self->windowClosestAcceptableGeometry(*nativeRect));
}

//  QRectF QPlatformWindow::closestAcceptableGeometry(const QWindow *w, const
//      QRectF &nativeRect)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN15QPlatformWindow25closestAcceptableGeometryEPK7QWindowRK6QRectF(
    const QWindow *w,
    const QRectF *nativeRect) {
  return new QRectF(
      QPlatformWindow::closestAcceptableGeometry(
          w,
          *nativeRect));
}

//  QString QPlatformWindow::formatWindowTitle(const QString &title, const
//      QString &separator)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QPlatformWindow17formatWindowTitleERK7QStringS2_(
    const QString *title,
    const QString *separator) {
  return new QString(QPlatformWindow::formatWindowTitle(*title, *separator));
}

//  QPlatformScreen *QPlatformWindow::screenForGeometry(const QRect
//      &newGeometry) const
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_ZNK15QPlatformWindow17screenForGeometryERK5QRect(
    const QPlatformWindow *self,
    const QRect *newGeometry) {
  return self->screenForGeometry(*newGeometry);
}

//  QSize QPlatformWindow::constrainWindowSize(const QSize &size)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN15QPlatformWindow19constrainWindowSizeERK5QSize(
    const QSize *size) {
  return new QSize(QPlatformWindow::constrainWindowSize(*size));
}

//  bool QPlatformWindow::isSubWindow(const QWindow *window)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPlatformWindow11isSubWindowEPK7QWindow(
    const QWindow *window) {
  return QPlatformWindow::isSubWindow(window);
}

//  a Python function taken by a CuteQPlatformWindow, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformWindow(
    QPlatformWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformWindow *>(self)->take(key, call);
}

//  void QPlatformWindow::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow10initializeEv(QPlatformWindow *self) {
  self->QPlatformWindow::initialize();
}

//  QPlatformScreen *QPlatformWindow::screen() const
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_own_ZNK15QPlatformWindow6screenEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::screen();
}

//  QSurfaceFormat QPlatformWindow::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_own_ZNK15QPlatformWindow6formatEv(
    const QPlatformWindow *self) {
  return new QSurfaceFormat(self->QPlatformWindow::format());
}

//  void QPlatformWindow::setGeometry(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow11setGeometryERK5QRect(
    QPlatformWindow *self,
    const QRect *rect) {
  self->QPlatformWindow::setGeometry(*rect);
}

//  QRect QPlatformWindow::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK15QPlatformWindow8geometryEv(
    const QPlatformWindow *self) {
  return new QRect(self->QPlatformWindow::geometry());
}

//  QRect QPlatformWindow::normalGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK15QPlatformWindow14normalGeometryEv(
    const QPlatformWindow *self) {
  return new QRect(self->QPlatformWindow::normalGeometry());
}

//  QMargins QPlatformWindow::frameMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_own_ZNK15QPlatformWindow12frameMarginsEv(
    const QPlatformWindow *self) {
  return new QMargins(self->QPlatformWindow::frameMargins());
}

//  QMargins QPlatformWindow::safeAreaMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_own_ZNK15QPlatformWindow15safeAreaMarginsEv(
    const QPlatformWindow *self) {
  return new QMargins(self->QPlatformWindow::safeAreaMargins());
}

//  void QPlatformWindow::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow10setVisibleEb(
    QPlatformWindow *self,
    bool visible) {
  self->QPlatformWindow::setVisible(visible);
}

//  void QPlatformWindow::setWindowFlags(Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QPlatformWindow *self,
    int flags) {
  self->QPlatformWindow::setWindowFlags(
      QFlags<Qt::WindowType>::fromInt(flags));
}

//  void QPlatformWindow::setWindowState(Qt::WindowStates state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow14setWindowStateE6QFlagsIN2Qt11WindowStateEE(
    QPlatformWindow *self,
    int state) {
  self->QPlatformWindow::setWindowState(
      QFlags<Qt::WindowState>::fromInt(state));
}

//  WId QPlatformWindow::winId() const
extern "C" Q_DECL_EXPORT
WId ritual_own_ZNK15QPlatformWindow5winIdEv(const QPlatformWindow *self) {
  return self->QPlatformWindow::winId();
}

//  void QPlatformWindow::setParent(const QPlatformWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow9setParentEPKS_(
    QPlatformWindow *self,
    const QPlatformWindow *window) {
  self->QPlatformWindow::setParent(window);
}

//  void QPlatformWindow::setWindowTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow14setWindowTitleERK7QString(
    QPlatformWindow *self,
    const QString *title) {
  self->QPlatformWindow::setWindowTitle(*title);
}

//  QString QPlatformWindow::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QPlatformWindow11windowTitleEv(
    const QPlatformWindow *self) {
  return new QString(self->QPlatformWindow::windowTitle());
}

//  void QPlatformWindow::setWindowFilePath(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow17setWindowFilePathERK7QString(
    QPlatformWindow *self,
    const QString *title) {
  self->QPlatformWindow::setWindowFilePath(*title);
}

//  void QPlatformWindow::setWindowIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow13setWindowIconERK5QIcon(
    QPlatformWindow *self,
    const QIcon *icon) {
  self->QPlatformWindow::setWindowIcon(*icon);
}

//  bool QPlatformWindow::close()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPlatformWindow5closeEv(QPlatformWindow *self) {
  return self->QPlatformWindow::close();
}

//  void QPlatformWindow::raise()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow5raiseEv(QPlatformWindow *self) {
  self->QPlatformWindow::raise();
}

//  void QPlatformWindow::lower()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow5lowerEv(QPlatformWindow *self) {
  self->QPlatformWindow::lower();
}

//  bool QPlatformWindow::isExposed() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformWindow9isExposedEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::isExposed();
}

//  bool QPlatformWindow::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformWindow8isActiveEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::isActive();
}

//  bool QPlatformWindow::isAncestorOf(const QPlatformWindow *child) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformWindow12isAncestorOfEPKS_(
    const QPlatformWindow *self,
    const QPlatformWindow *child) {
  return self->QPlatformWindow::isAncestorOf(child);
}

//  bool QPlatformWindow::isEmbedded() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformWindow10isEmbeddedEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::isEmbedded();
}

//  bool QPlatformWindow::isForeignWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformWindow15isForeignWindowEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::isForeignWindow();
}

//  QPoint QPlatformWindow::mapToGlobal(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK15QPlatformWindow11mapToGlobalERK6QPoint(
    const QPlatformWindow *self,
    const QPoint *pos) {
  return new QPoint(self->QPlatformWindow::mapToGlobal(*pos));
}

//  QPoint QPlatformWindow::mapFromGlobal(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK15QPlatformWindow13mapFromGlobalERK6QPoint(
    const QPlatformWindow *self,
    const QPoint *pos) {
  return new QPoint(self->QPlatformWindow::mapFromGlobal(*pos));
}

//  void QPlatformWindow::propagateSizeHints()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow18propagateSizeHintsEv(
    QPlatformWindow *self) {
  self->QPlatformWindow::propagateSizeHints();
}

//  void QPlatformWindow::setOpacity(qreal level)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow10setOpacityEd(
    QPlatformWindow *self,
    qreal level) {
  self->QPlatformWindow::setOpacity(level);
}

//  void QPlatformWindow::setMask(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow7setMaskERK7QRegion(
    QPlatformWindow *self,
    const QRegion *region) {
  self->QPlatformWindow::setMask(*region);
}

//  void QPlatformWindow::requestActivateWindow()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow21requestActivateWindowEv(
    QPlatformWindow *self) {
  self->QPlatformWindow::requestActivateWindow();
}

//  void
//      QPlatformWindow::handleContentOrientationChange(Qt::ScreenOrientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow30handleContentOrientationChangeEN2Qt17ScreenOrientationE(
    QPlatformWindow *self,
    Qt::ScreenOrientation orientation) {
  self->QPlatformWindow::handleContentOrientationChange(orientation);
}

//  qreal QPlatformWindow::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK15QPlatformWindow16devicePixelRatioEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::devicePixelRatio();
}

//  bool QPlatformWindow::setKeyboardGrabEnabled(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPlatformWindow22setKeyboardGrabEnabledEb(
    QPlatformWindow *self,
    bool grab) {
  return self->QPlatformWindow::setKeyboardGrabEnabled(grab);
}

//  bool QPlatformWindow::setMouseGrabEnabled(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPlatformWindow19setMouseGrabEnabledEb(
    QPlatformWindow *self,
    bool grab) {
  return self->QPlatformWindow::setMouseGrabEnabled(grab);
}

//  bool QPlatformWindow::setWindowModified(bool modified)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPlatformWindow17setWindowModifiedEb(
    QPlatformWindow *self,
    bool modified) {
  return self->QPlatformWindow::setWindowModified(modified);
}

//  bool QPlatformWindow::windowEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPlatformWindow11windowEventEP6QEvent(
    QPlatformWindow *self,
    QEvent *event) {
  return self->QPlatformWindow::windowEvent(event);
}

//  bool QPlatformWindow::startSystemResize(Qt::Edges edges)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPlatformWindow17startSystemResizeE6QFlagsIN2Qt4EdgeEE(
    QPlatformWindow *self,
    int edges) {
  return self->QPlatformWindow::startSystemResize(
      QFlags<Qt::Edge>::fromInt(edges));
}

//  bool QPlatformWindow::startSystemMove()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPlatformWindow15startSystemMoveEv(
    QPlatformWindow *self) {
  return self->QPlatformWindow::startSystemMove();
}

//  void QPlatformWindow::setFrameStrutEventsEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow26setFrameStrutEventsEnabledEb(
    QPlatformWindow *self,
    bool enabled) {
  self->QPlatformWindow::setFrameStrutEventsEnabled(enabled);
}

//  bool QPlatformWindow::frameStrutEventsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformWindow23frameStrutEventsEnabledEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::frameStrutEventsEnabled();
}

//  void QPlatformWindow::setAlertState(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow13setAlertStateEb(
    QPlatformWindow *self,
    bool enabled) {
  self->QPlatformWindow::setAlertState(enabled);
}

//  bool QPlatformWindow::isAlertState() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformWindow12isAlertStateEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::isAlertState();
}

//  void QPlatformWindow::invalidateSurface()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow17invalidateSurfaceEv(
    QPlatformWindow *self) {
  self->QPlatformWindow::invalidateSurface();
}

//  void QPlatformWindow::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow13requestUpdateEv(QPlatformWindow *self) {
  self->QPlatformWindow::requestUpdate();
}

//  void QPlatformWindow::deliverUpdateRequest()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformWindow20deliverUpdateRequestEv(
    QPlatformWindow *self) {
  self->QPlatformWindow::deliverUpdateRequest();
}

//  bool QPlatformWindow::allowsIndependentThreadedRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QPlatformWindow34allowsIndependentThreadedRenderingEv(
    const QPlatformWindow *self) {
  return self->QPlatformWindow::allowsIndependentThreadedRendering();
}
