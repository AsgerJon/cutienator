//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractintegration.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractintegration.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDesignerIntegration that Python can take functions over in. Every QDesignerIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQDesignerIntegrationCall0)(const void *, int *);
typedef void (*CuteQDesignerIntegrationCall1)(const void *, const QString *, int *);
typedef bool (*CuteQDesignerIntegrationCall2)(const void *, int *);
typedef void (*CuteQDesignerIntegrationCall3)(const void *, bool, int *);
typedef int (*CuteQDesignerIntegrationCall4)(const void *, int *);
typedef void (*CuteQDesignerIntegrationCall5)(const void *, int, int *);
typedef int (*CuteQDesignerIntegrationCall6)(const void *, int *);
typedef void (*CuteQDesignerIntegrationCall7)(const void *, int, int *);
typedef void * (*CuteQDesignerIntegrationCall8)(const void *, QWidget *, int *);
typedef void * (*CuteQDesignerIntegrationCall9)(const void *, QWidget *, int *);
typedef QString * (*CuteQDesignerIntegrationCall10)(const void *, int *);
typedef void (*CuteQDesignerIntegrationCall11)(const void *, const QString *, const QVariant *, bool, int *);
typedef void (*CuteQDesignerIntegrationCall12)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQDesignerIntegrationCall13)(const void *, const QString *, int *);
typedef void (*CuteQDesignerIntegrationCall14)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQDesignerIntegrationCall15)(const void *, const QString *, int *);
typedef void (*CuteQDesignerIntegrationCall16)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*CuteQDesignerIntegrationCall17)(const void *, QDesignerFormWindowInterface *, int *);
typedef void (*CuteQDesignerIntegrationCall18)(const void *, int *);
typedef void (*CuteQDesignerIntegrationCall19)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerIntegrationCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDesignerIntegrationCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDesignerIntegrationCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDesignerIntegration : public QDesignerIntegration {
public:
  using QDesignerIntegration::QDesignerIntegration;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface12headerSuffixEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface15setHeaderSuffixERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface17isHeaderLowercaseEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface18setHeaderLowercaseEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface8featuresEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface11setFeaturesE6QFlagsINS_11FeatureFlagEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface28resourceFileWatcherBehaviourEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface31setResourceFileWatcherBehaviourENS_28ResourceFileWatcherBehaviourE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface15containerWindowEP7QWidget")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface21createResourceBrowserEP7QWidget")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QDesignerIntegrationInterface13contextHelpIdEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStringRK8QVariantb")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface14updatePropertyERK7QStringRK8QVariant")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface13resetPropertyERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface18addDynamicPropertyERK7QStringRK8QVariant")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface21removeDynamicPropertyERK7QString")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface22updateActiveFormWindowEP28QDesignerFormWindowInterface")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface15setupFormWindowEP28QDesignerFormWindowInterface")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface15updateSelectionEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerIntegrationInterface25updateCustomWidgetPluginsEv")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QString QDesignerIntegration::headerSuffix() const
  QString headerSuffix() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerIntegrationCall0 call = reinterpret_cast<CuteQDesignerIntegrationCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerIntegration::headerSuffix();
  }

  //  void QDesignerIntegration::setHeaderSuffix(const QString
  //      &headerSuffix)
  void setHeaderSuffix(const QString &headerSuffix) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerIntegrationCall1 call = reinterpret_cast<CuteQDesignerIntegrationCall1>(taken[1]);
      call(this, &headerSuffix, &handled);
      if (handled) return;
    }
    QDesignerIntegration::setHeaderSuffix(headerSuffix);
  }

  //  bool QDesignerIntegration::isHeaderLowercase() const
  bool isHeaderLowercase() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerIntegrationCall2 call = reinterpret_cast<CuteQDesignerIntegrationCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QDesignerIntegration::isHeaderLowercase();
  }

  //  void QDesignerIntegration::setHeaderLowercase(bool headerLowerCase)
  void setHeaderLowercase(bool headerLowerCase) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerIntegrationCall3 call = reinterpret_cast<CuteQDesignerIntegrationCall3>(taken[3]);
      call(this, headerLowerCase, &handled);
      if (handled) return;
    }
    QDesignerIntegration::setHeaderLowercase(headerLowerCase);
  }

  //  Feature QDesignerIntegration::features() const
  QDesignerIntegrationInterface::Feature features() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerIntegrationCall4 call = reinterpret_cast<CuteQDesignerIntegrationCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<QDesignerIntegrationInterface::FeatureFlag>::fromInt(given);
    }
    return QDesignerIntegration::features();
  }

  //  void QDesignerIntegration::setFeatures(Feature f)
  void setFeatures(QDesignerIntegrationInterface::Feature f) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerIntegrationCall5 call = reinterpret_cast<CuteQDesignerIntegrationCall5>(taken[5]);
      call(this, static_cast<int>(f.toInt()), &handled);
      if (handled) return;
    }
    QDesignerIntegration::setFeatures(f);
  }

  //  ResourceFileWatcherBehaviour
  //      QDesignerIntegration::resourceFileWatcherBehaviour() const
  QDesignerIntegrationInterface::ResourceFileWatcherBehaviour resourceFileWatcherBehaviour() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesignerIntegrationCall6 call = reinterpret_cast<CuteQDesignerIntegrationCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerIntegrationInterface::ResourceFileWatcherBehaviour>(given);
    }
    return QDesignerIntegration::resourceFileWatcherBehaviour();
  }

  //  void QDesignerIntegration::setResourceFileWatcherBehaviour(ResourceFi
  //      leWatcherBehaviour behaviour)
  void setResourceFileWatcherBehaviour(
      QDesignerIntegrationInterface::ResourceFileWatcherBehaviour behaviour) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesignerIntegrationCall7 call = reinterpret_cast<CuteQDesignerIntegrationCall7>(taken[7]);
      call(this, static_cast<int>(behaviour), &handled);
      if (handled) return;
    }
    QDesignerIntegration::setResourceFileWatcherBehaviour(behaviour);
  }

  //  QWidget *QDesignerIntegration::containerWindow(QWidget *widget) const
  QWidget *containerWindow(QWidget *widget) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDesignerIntegrationCall8 call = reinterpret_cast<CuteQDesignerIntegrationCall8>(taken[8]);
      void * given = call(this, widget, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QDesignerIntegration::containerWindow(widget);
  }

  //  QDesignerResourceBrowserInterface
  //      *QDesignerIntegration::createResourceBrowser(QWidget *parent)
  QDesignerResourceBrowserInterface *createResourceBrowser(
      QWidget *parent) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDesignerIntegrationCall9 call = reinterpret_cast<CuteQDesignerIntegrationCall9>(taken[9]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QDesignerResourceBrowserInterface *>(given);
    }
    return QDesignerIntegration::createResourceBrowser(parent);
  }

  //  QString QDesignerIntegration::contextHelpId() const
  QString contextHelpId() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDesignerIntegrationCall10 call = reinterpret_cast<CuteQDesignerIntegrationCall10>(taken[10]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesignerIntegration::contextHelpId();
  }

  //  void QDesignerIntegration::updateProperty(const QString &name, const
  //      QVariant &value, bool enableSubPropertyHandling)
  void updateProperty(
      const QString &name,
      const QVariant &value,
      bool enableSubPropertyHandling) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDesignerIntegrationCall11 call = reinterpret_cast<CuteQDesignerIntegrationCall11>(taken[11]);
      call(this, &name, &value, enableSubPropertyHandling, &handled);
      if (handled) return;
    }
    QDesignerIntegration::updateProperty(name, value, enableSubPropertyHandling);
  }

  //  void QDesignerIntegration::updateProperty(const QString &name, const
  //      QVariant &value)
  void updateProperty(const QString &name, const QVariant &value) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDesignerIntegrationCall12 call = reinterpret_cast<CuteQDesignerIntegrationCall12>(taken[12]);
      call(this, &name, &value, &handled);
      if (handled) return;
    }
    QDesignerIntegration::updateProperty(name, value);
  }

  //  void QDesignerIntegration::resetProperty(const QString &name)
  void resetProperty(const QString &name) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDesignerIntegrationCall13 call = reinterpret_cast<CuteQDesignerIntegrationCall13>(taken[13]);
      call(this, &name, &handled);
      if (handled) return;
    }
    QDesignerIntegration::resetProperty(name);
  }

  //  void QDesignerIntegration::addDynamicProperty(const QString &name,
  //      const QVariant &value)
  void addDynamicProperty(
      const QString &name,
      const QVariant &value) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDesignerIntegrationCall14 call = reinterpret_cast<CuteQDesignerIntegrationCall14>(taken[14]);
      call(this, &name, &value, &handled);
      if (handled) return;
    }
    QDesignerIntegration::addDynamicProperty(name, value);
  }

  //  void QDesignerIntegration::removeDynamicProperty(const QString &name)
  void removeDynamicProperty(const QString &name) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDesignerIntegrationCall15 call = reinterpret_cast<CuteQDesignerIntegrationCall15>(taken[15]);
      call(this, &name, &handled);
      if (handled) return;
    }
    QDesignerIntegration::removeDynamicProperty(name);
  }

  //  void QDesignerIntegration::updateActiveFormWindow(QDesignerFormWindow
  //      Interface *formWindow)
  void updateActiveFormWindow(
      QDesignerFormWindowInterface *formWindow) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDesignerIntegrationCall16 call = reinterpret_cast<CuteQDesignerIntegrationCall16>(taken[16]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
    QDesignerIntegration::updateActiveFormWindow(formWindow);
  }

  //  void
  //      QDesignerIntegration::setupFormWindow(QDesignerFormWindowInterfac
  //      e *formWindow)
  void setupFormWindow(QDesignerFormWindowInterface *formWindow) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDesignerIntegrationCall17 call = reinterpret_cast<CuteQDesignerIntegrationCall17>(taken[17]);
      call(this, formWindow, &handled);
      if (handled) return;
    }
    QDesignerIntegration::setupFormWindow(formWindow);
  }

  //  void QDesignerIntegration::updateSelection()
  void updateSelection() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDesignerIntegrationCall18 call = reinterpret_cast<CuteQDesignerIntegrationCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QDesignerIntegration::updateSelection();
  }

  //  void QDesignerIntegration::updateCustomWidgetPlugins()
  void updateCustomWidgetPlugins() override {
    if (taken[19]) {
      int handled = 0;
      CuteQDesignerIntegrationCall19 call = reinterpret_cast<CuteQDesignerIntegrationCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QDesignerIntegration::updateCustomWidgetPlugins();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDesignerIntegrationCall20 call = reinterpret_cast<CuteQDesignerIntegrationCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDesignerIntegrationCall21 call = reinterpret_cast<CuteQDesignerIntegrationCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDesignerIntegrationCall22 call = reinterpret_cast<CuteQDesignerIntegrationCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDesignerIntegrationCall23 call = reinterpret_cast<CuteQDesignerIntegrationCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDesignerIntegrationCall24 call = reinterpret_cast<CuteQDesignerIntegrationCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDesignerIntegrationCall25 call = reinterpret_cast<CuteQDesignerIntegrationCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDesignerIntegrationCall26 call = reinterpret_cast<CuteQDesignerIntegrationCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDesignerIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QDesignerIntegration10metaObjectEv(
    const QDesignerIntegration *self) {
  return self->metaObject();
}

//  QString QDesignerIntegration::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QDesignerIntegration2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDesignerIntegration::tr(s, c, n));
}

//  QDesignerIntegration::QDesignerIntegration(QDesignerFormEditorInterface
//      *core, QObject *parent)
extern "C" Q_DECL_EXPORT
QDesignerIntegration *ritual_ZN20QDesignerIntegrationC1EP28QDesignerFormEditorInterfaceP7QObject(
    QDesignerFormEditorInterface *core,
    QObject *parent) {
  return new CuteQDesignerIntegration(core, parent);
}

//  QDesignerIntegration::~QDesignerIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegrationD1Ev(QDesignerIntegration *self) {
  delete self;
}

//  QString QDesignerIntegration::headerSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDesignerIntegration12headerSuffixEv(
    const QDesignerIntegration *self) {
  return new QString(self->headerSuffix());
}

//  void QDesignerIntegration::setHeaderSuffix(const QString &headerSuffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration15setHeaderSuffixERK7QString(
    QDesignerIntegration *self,
    const QString *headerSuffix) {
  self->setHeaderSuffix(*headerSuffix);
}

//  bool QDesignerIntegration::isHeaderLowercase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDesignerIntegration17isHeaderLowercaseEv(
    const QDesignerIntegration *self) {
  return self->isHeaderLowercase();
}

//  void QDesignerIntegration::setHeaderLowercase(bool headerLowerCase)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration18setHeaderLowercaseEb(
    QDesignerIntegration *self,
    bool headerLowerCase) {
  self->setHeaderLowercase(headerLowerCase);
}

//  Feature QDesignerIntegration::features() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDesignerIntegration8featuresEv(
    const QDesignerIntegration *self) {
  return static_cast<int>(self->features().toInt());
}

//  void QDesignerIntegration::setFeatures(Feature f)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration11setFeaturesE6QFlagsIN29QDesignerIntegrationInterface11FeatureFlagEE(
    QDesignerIntegration *self,
    int f) {
  self->setFeatures(
      QFlags<QDesignerIntegrationInterface::FeatureFlag>::fromInt(f));
}

//  ResourceFileWatcherBehaviour
//      QDesignerIntegration::resourceFileWatcherBehaviour() const
extern "C" Q_DECL_EXPORT
QDesignerIntegrationInterface::ResourceFileWatcherBehaviour ritual_ZNK20QDesignerIntegration28resourceFileWatcherBehaviourEv(
    const QDesignerIntegration *self) {
  return self->resourceFileWatcherBehaviour();
}

//  void QDesignerIntegration::setResourceFileWatcherBehaviour(ResourceFileWa
//      tcherBehaviour behaviour)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration31setResourceFileWatcherBehaviourEN29QDesignerIntegrationInterface28ResourceFileWatcherBehaviourE(
    QDesignerIntegration *self,
    QDesignerIntegrationInterface::ResourceFileWatcherBehaviour behaviour) {
  self->setResourceFileWatcherBehaviour(behaviour);
}

//  QWidget *QDesignerIntegration::containerWindow(QWidget *widget) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK20QDesignerIntegration15containerWindowEP7QWidget(
    const QDesignerIntegration *self,
    QWidget *widget) {
  return self->containerWindow(widget);
}

//  void QDesignerIntegration::initializePlugins(QDesignerFormEditorInterface
//      *formEditor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration17initializePluginsEP28QDesignerFormEditorInterface(
    QDesignerFormEditorInterface *formEditor) {
  QDesignerIntegration::initializePlugins(formEditor);
}

//  QDesignerResourceBrowserInterface
//      *QDesignerIntegration::createResourceBrowser(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDesignerResourceBrowserInterface *ritual_ZN20QDesignerIntegration21createResourceBrowserEP7QWidget(
    QDesignerIntegration *self,
    QWidget *parent) {
  return self->createResourceBrowser(parent);
}

//  QString QDesignerIntegration::contextHelpId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDesignerIntegration13contextHelpIdEv(
    const QDesignerIntegration *self) {
  return new QString(self->contextHelpId());
}

//  void QDesignerIntegration::updateProperty(const QString &name, const
//      QVariant &value, bool enableSubPropertyHandling)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration14updatePropertyERK7QStringRK8QVariantb(
    QDesignerIntegration *self,
    const QString *name,
    const QVariant *value,
    bool enableSubPropertyHandling) {
  self->updateProperty(*name, *value, enableSubPropertyHandling);
}

//  void QDesignerIntegration::updateProperty(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration14updatePropertyERK7QStringRK8QVariant(
    QDesignerIntegration *self,
    const QString *name,
    const QVariant *value) {
  self->updateProperty(*name, *value);
}

//  void QDesignerIntegration::resetProperty(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration13resetPropertyERK7QString(
    QDesignerIntegration *self,
    const QString *name) {
  self->resetProperty(*name);
}

//  void QDesignerIntegration::addDynamicProperty(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration18addDynamicPropertyERK7QStringRK8QVariant(
    QDesignerIntegration *self,
    const QString *name,
    const QVariant *value) {
  self->addDynamicProperty(*name, *value);
}

//  void QDesignerIntegration::removeDynamicProperty(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration21removeDynamicPropertyERK7QString(
    QDesignerIntegration *self,
    const QString *name) {
  self->removeDynamicProperty(*name);
}

//  void
//      QDesignerIntegration::updateActiveFormWindow(QDesignerFormWindowInter
//      face *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration22updateActiveFormWindowEP28QDesignerFormWindowInterface(
    QDesignerIntegration *self,
    QDesignerFormWindowInterface *formWindow) {
  self->updateActiveFormWindow(formWindow);
}

//  void QDesignerIntegration::setupFormWindow(QDesignerFormWindowInterface
//      *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration15setupFormWindowEP28QDesignerFormWindowInterface(
    QDesignerIntegration *self,
    QDesignerFormWindowInterface *formWindow) {
  self->setupFormWindow(formWindow);
}

//  void QDesignerIntegration::updateSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration15updateSelectionEv(
    QDesignerIntegration *self) {
  self->updateSelection();
}

//  void QDesignerIntegration::updateCustomWidgetPlugins()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesignerIntegration25updateCustomWidgetPluginsEv(
    QDesignerIntegration *self) {
  self->updateCustomWidgetPlugins();
}

//  a Python function taken by a CuteQDesignerIntegration, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerIntegration(
    QDesignerIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerIntegration *>(self)->take(key, call);
}

//  QString QDesignerIntegration::headerSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QDesignerIntegration12headerSuffixEv(
    const QDesignerIntegration *self) {
  return new QString(self->QDesignerIntegration::headerSuffix());
}

//  void QDesignerIntegration::setHeaderSuffix(const QString &headerSuffix)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration15setHeaderSuffixERK7QString(
    QDesignerIntegration *self,
    const QString *headerSuffix) {
  self->QDesignerIntegration::setHeaderSuffix(*headerSuffix);
}

//  bool QDesignerIntegration::isHeaderLowercase() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QDesignerIntegration17isHeaderLowercaseEv(
    const QDesignerIntegration *self) {
  return self->QDesignerIntegration::isHeaderLowercase();
}

//  void QDesignerIntegration::setHeaderLowercase(bool headerLowerCase)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration18setHeaderLowercaseEb(
    QDesignerIntegration *self,
    bool headerLowerCase) {
  self->QDesignerIntegration::setHeaderLowercase(headerLowerCase);
}

//  Feature QDesignerIntegration::features() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QDesignerIntegration8featuresEv(
    const QDesignerIntegration *self) {
  return static_cast<int>(self->QDesignerIntegration::features().toInt());
}

//  void QDesignerIntegration::setFeatures(Feature f)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration11setFeaturesE6QFlagsIN29QDesignerIntegrationInterface11FeatureFlagEE(
    QDesignerIntegration *self,
    int f) {
  self->QDesignerIntegration::setFeatures(
      QFlags<QDesignerIntegrationInterface::FeatureFlag>::fromInt(f));
}

//  ResourceFileWatcherBehaviour
//      QDesignerIntegration::resourceFileWatcherBehaviour() const
extern "C" Q_DECL_EXPORT
QDesignerIntegrationInterface::ResourceFileWatcherBehaviour ritual_own_ZNK20QDesignerIntegration28resourceFileWatcherBehaviourEv(
    const QDesignerIntegration *self) {
  return self->QDesignerIntegration::resourceFileWatcherBehaviour();
}

//  void QDesignerIntegration::setResourceFileWatcherBehaviour(ResourceFileWa
//      tcherBehaviour behaviour)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration31setResourceFileWatcherBehaviourEN29QDesignerIntegrationInterface28ResourceFileWatcherBehaviourE(
    QDesignerIntegration *self,
    QDesignerIntegrationInterface::ResourceFileWatcherBehaviour behaviour) {
  self->QDesignerIntegration::setResourceFileWatcherBehaviour(behaviour);
}

//  QWidget *QDesignerIntegration::containerWindow(QWidget *widget) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK20QDesignerIntegration15containerWindowEP7QWidget(
    const QDesignerIntegration *self,
    QWidget *widget) {
  return self->QDesignerIntegration::containerWindow(widget);
}

//  QDesignerResourceBrowserInterface
//      *QDesignerIntegration::createResourceBrowser(QWidget *parent)
extern "C" Q_DECL_EXPORT
QDesignerResourceBrowserInterface *ritual_own_ZN20QDesignerIntegration21createResourceBrowserEP7QWidget(
    QDesignerIntegration *self,
    QWidget *parent) {
  return self->QDesignerIntegration::createResourceBrowser(parent);
}

//  QString QDesignerIntegration::contextHelpId() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QDesignerIntegration13contextHelpIdEv(
    const QDesignerIntegration *self) {
  return new QString(self->QDesignerIntegration::contextHelpId());
}

//  void QDesignerIntegration::updateProperty(const QString &name, const
//      QVariant &value, bool enableSubPropertyHandling)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration14updatePropertyERK7QStringRK8QVariantb(
    QDesignerIntegration *self,
    const QString *name,
    const QVariant *value,
    bool enableSubPropertyHandling) {
  self->QDesignerIntegration::updateProperty(
      *name,
      *value,
      enableSubPropertyHandling);
}

//  void QDesignerIntegration::updateProperty(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration14updatePropertyERK7QStringRK8QVariant(
    QDesignerIntegration *self,
    const QString *name,
    const QVariant *value) {
  self->QDesignerIntegration::updateProperty(*name, *value);
}

//  void QDesignerIntegration::resetProperty(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration13resetPropertyERK7QString(
    QDesignerIntegration *self,
    const QString *name) {
  self->QDesignerIntegration::resetProperty(*name);
}

//  void QDesignerIntegration::addDynamicProperty(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration18addDynamicPropertyERK7QStringRK8QVariant(
    QDesignerIntegration *self,
    const QString *name,
    const QVariant *value) {
  self->QDesignerIntegration::addDynamicProperty(*name, *value);
}

//  void QDesignerIntegration::removeDynamicProperty(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration21removeDynamicPropertyERK7QString(
    QDesignerIntegration *self,
    const QString *name) {
  self->QDesignerIntegration::removeDynamicProperty(*name);
}

//  void
//      QDesignerIntegration::updateActiveFormWindow(QDesignerFormWindowInter
//      face *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration22updateActiveFormWindowEP28QDesignerFormWindowInterface(
    QDesignerIntegration *self,
    QDesignerFormWindowInterface *formWindow) {
  self->QDesignerIntegration::updateActiveFormWindow(formWindow);
}

//  void QDesignerIntegration::setupFormWindow(QDesignerFormWindowInterface
//      *formWindow)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration15setupFormWindowEP28QDesignerFormWindowInterface(
    QDesignerIntegration *self,
    QDesignerFormWindowInterface *formWindow) {
  self->QDesignerIntegration::setupFormWindow(formWindow);
}

//  void QDesignerIntegration::updateSelection()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration15updateSelectionEv(
    QDesignerIntegration *self) {
  self->QDesignerIntegration::updateSelection();
}

//  void QDesignerIntegration::updateCustomWidgetPlugins()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesignerIntegration25updateCustomWidgetPluginsEv(
    QDesignerIntegration *self) {
  self->QDesignerIntegration::updateCustomWidgetPlugins();
}
