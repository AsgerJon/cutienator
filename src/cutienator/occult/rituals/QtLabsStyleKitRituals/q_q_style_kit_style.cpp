//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitstyle_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQStyleKitStyle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQStyleKitStyle : QQStyleKitStyle {
  using QQStyleKitStyle::componentComplete;
};

//  A QQStyleKitStyle that Python can take functions over in. Every QQStyleKitStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQStyleKitStyleCall0)(const void *, int *);
typedef void (*CuteQQStyleKitStyleCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitStyleCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQStyleKitStyleCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitStyleCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitStyleCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitStyleCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitStyleCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQStyleKitStyleCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQStyleKitStyle : public QQStyleKitStyle {
public:
  using QQStyleKitStyle::QQStyleKitStyle;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQStyleKitStyle::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQStyleKitStyleCall0 call = reinterpret_cast<CuteQQStyleKitStyleCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQStyleKitStyle::componentComplete();
  }

  //  void QQStyleKitControls::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQStyleKitStyleCall1 call = reinterpret_cast<CuteQQStyleKitStyleCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQStyleKitControls::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQStyleKitStyleCall2 call = reinterpret_cast<CuteQQStyleKitStyleCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQStyleKitStyleCall3 call = reinterpret_cast<CuteQQStyleKitStyleCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQStyleKitStyleCall4 call = reinterpret_cast<CuteQQStyleKitStyleCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQStyleKitStyleCall5 call = reinterpret_cast<CuteQQStyleKitStyleCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQStyleKitStyleCall6 call = reinterpret_cast<CuteQQStyleKitStyleCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQStyleKitStyleCall7 call = reinterpret_cast<CuteQQStyleKitStyleCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQStyleKitStyleCall8 call = reinterpret_cast<CuteQQStyleKitStyleCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQStyleKitStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQStyleKitStyle10metaObjectEv(
    const QQStyleKitStyle *self) {
  return self->metaObject();
}

//  QString QQStyleKitStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQStyleKitStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQStyleKitStyle::tr(s, c, n));
}

//  QQStyleKitStyle::QQStyleKitStyle(QObject *parent)
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZN15QQStyleKitStyleC1EP7QObject(QObject *parent) {
  return new CuteQQStyleKitStyle(parent);
}

//  QQStyleKitStyle::~QQStyleKitStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyleD1Ev(QQStyleKitStyle *self) {
  delete self;
}

//  QQuickPalette *QQStyleKitStyle::palette() const
extern "C" Q_DECL_EXPORT
QQuickPalette *ritual_ZNK15QQStyleKitStyle7paletteEv(
    const QQStyleKitStyle *self) {
  return self->palette();
}

//  QQStyleKitStyle *QQStyleKitStyle::fallbackStyle() const
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZNK15QQStyleKitStyle13fallbackStyleEv(
    const QQStyleKitStyle *self) {
  return self->fallbackStyle();
}

//  void QQStyleKitStyle::setFallbackStyle(QQStyleKitStyle *fallbackStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle16setFallbackStyleEPS_(
    QQStyleKitStyle *self,
    QQStyleKitStyle *fallbackStyle) {
  self->setFallbackStyle(fallbackStyle);
}

//  QQmlComponent *QQStyleKitStyle::light() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK15QQStyleKitStyle5lightEv(
    const QQStyleKitStyle *self) {
  return self->light();
}

//  void QQStyleKitStyle::setLight(QQmlComponent *lightTheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle8setLightEP13QQmlComponent(
    QQStyleKitStyle *self,
    QQmlComponent *lightTheme) {
  self->setLight(lightTheme);
}

//  QQmlComponent *QQStyleKitStyle::dark() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK15QQStyleKitStyle4darkEv(
    const QQStyleKitStyle *self) {
  return self->dark();
}

//  void QQStyleKitStyle::setDark(QQmlComponent *darkTheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle7setDarkEP13QQmlComponent(
    QQStyleKitStyle *self,
    QQmlComponent *darkTheme) {
  self->setDark(darkTheme);
}

//  QList<QQStyleKitCustomTheme *> QQStyleKitStyle::customThemes() const
extern "C" Q_DECL_EXPORT
QList<QQStyleKitCustomTheme *> *ritual_ZNK15QQStyleKitStyle12customThemesEv(
    const QQStyleKitStyle *self) {
  return new QList<QQStyleKitCustomTheme *>(self->customThemes());
}

//  QStringList QQStyleKitStyle::availableThemeNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QQStyleKitStyle19availableThemeNamesEv(
    const QQStyleKitStyle *self) {
  return new QList<QString>(self->availableThemeNames());
}

//  QStringList QQStyleKitStyle::customThemeNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QQStyleKitStyle16customThemeNamesEv(
    const QQStyleKitStyle *self) {
  return new QList<QString>(self->customThemeNames());
}

//  void QQStyleKitStyle::setThemeName(const QString &themeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle12setThemeNameERK7QString(
    QQStyleKitStyle *self,
    const QString *themeName) {
  self->setThemeName(*themeName);
}

//  QString QQStyleKitStyle::themeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQStyleKitStyle9themeNameEv(
    const QQStyleKitStyle *self) {
  return new QString(self->themeName());
}

//  QQStyleKitTheme *QQStyleKitStyle::theme() const
extern "C" Q_DECL_EXPORT
QQStyleKitTheme *ritual_ZNK15QQStyleKitStyle5themeEv(
    const QQStyleKitStyle *self) {
  return self->theme();
}

//  void QQStyleKitStyle::recreateTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle13recreateThemeEv(QQStyleKitStyle *self) {
  self->recreateTheme();
}

//  bool QQStyleKitStyle::loaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQStyleKitStyle6loadedEv(const QQStyleKitStyle *self) {
  return self->loaded();
}

//  QQStyleKitStyle *QQStyleKitStyle::current()
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZN15QQStyleKitStyle7currentEv() {
  return QQStyleKitStyle::current();
}

//  QPalette
//      QQStyleKitStyle::paletteForControlType(QQStyleKitExtendableControlTyp
//      e type) const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK15QQStyleKitStyle21paletteForControlTypeEj(
    const QQStyleKitStyle *self,
    QQStyleKitExtendableControlType type) {
  return new QPalette(self->paletteForControlType(type));
}

//  QFont QQStyleKitStyle::fontForControlType(QQStyleKitExtendableControlType
//      type) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QQStyleKitStyle18fontForControlTypeEj(
    const QQStyleKitStyle *self,
    QQStyleKitExtendableControlType type) {
  return new QFont(self->fontForControlType(type));
}

//  void QQStyleKitStyle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle17componentCompleteEv(QQStyleKitStyle *self) {
  self->componentComplete();
}

//  void QQStyleKitStyle::parseThemes()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle11parseThemesEv(QQStyleKitStyle *self) {
  self->parseThemes();
}

//  void QQStyleKitStyle::reapplyStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle12reapplyStyleEv(QQStyleKitStyle *self) {
  self->reapplyStyle();
}

//  void QQStyleKitStyle::executeFallbackStyle(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle20executeFallbackStyleEb(
    QQStyleKitStyle *self,
    bool complete) {
  self->executeFallbackStyle(complete);
}

//  void QQStyleKitStyle::syncFromQPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitStyle16syncFromQPaletteERK8QPalette(
    QQStyleKitStyle *self,
    const QPalette *palette) {
  self->syncFromQPalette(*palette);
}

//  QPalette QQStyleKitStyle::effectivePalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK15QQStyleKitStyle16effectivePaletteEv(
    const QQStyleKitStyle *self) {
  return new QPalette(self->effectivePalette());
}

//  a Python function taken by a CuteQQStyleKitStyle, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQStyleKitStyle(
    QQStyleKitStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQStyleKitStyle *>(self)->take(key, call);
}

//  void QQStyleKitStyle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQStyleKitStyle17componentCompleteEv(
    QQStyleKitStyle *self) {
  static_cast<OwnQQStyleKitStyle *>(self)->OwnQQStyleKitStyle::componentComplete();
}
