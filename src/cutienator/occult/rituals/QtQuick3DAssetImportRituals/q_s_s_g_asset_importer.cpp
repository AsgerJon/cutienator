//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DAsset
//  Import/6.12.0/QtQuick3DAssetImport/private/qssgassetimporter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qtquick3dassetimportglobal_p.h>
#include <QtQuick3DAssetImport/QtQuick3DAssetImport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetImport/6.12.0/QtQuick3DAssetImport/private/qssgassetimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSSGAssetImporter that Python can take functions over in. Every QSSGAssetImporter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQSSGAssetImporterCall0)(const void *, int *);
typedef QString * (*CuteQSSGAssetImporterCall1)(const void *, int *);
typedef QString * (*CuteQSSGAssetImporterCall2)(const void *, int *);
typedef const QJsonObject * (*CuteQSSGAssetImporterCall3)(const void *, int *);
typedef QString * (*CuteQSSGAssetImporterCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSSGAssetImporterCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSSGAssetImporterCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImporterCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImporterCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImporterCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImporterCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSSGAssetImporterCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSSGAssetImporter : public QSSGAssetImporter {
public:
  using QSSGAssetImporter::QSSGAssetImporter;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QSSGAssetImporter4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QSSGAssetImporter15outputExtensionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QSSGAssetImporter4typeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QSSGAssetImporter13importOptionsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QSSGAssetImporter15typeDescriptionEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QString QSSGAssetImporter::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSSGAssetImporterCall0 call = reinterpret_cast<CuteQSSGAssetImporterCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QSSGAssetImporter::outputExtension() const
  QString outputExtension() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSSGAssetImporterCall1 call = reinterpret_cast<CuteQSSGAssetImporterCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QSSGAssetImporter::type() const
  QString type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSSGAssetImporterCall2 call = reinterpret_cast<CuteQSSGAssetImporterCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QJsonObject QSSGAssetImporter::importOptions() const
  QJsonObject importOptions() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSSGAssetImporterCall3 call = reinterpret_cast<CuteQSSGAssetImporterCall3>(taken[3]);
      const QJsonObject * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QString QSSGAssetImporter::typeDescription() const
  QString typeDescription() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSSGAssetImporterCall4 call = reinterpret_cast<CuteQSSGAssetImporterCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSSGAssetImporterCall5 call = reinterpret_cast<CuteQSSGAssetImporterCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSSGAssetImporterCall6 call = reinterpret_cast<CuteQSSGAssetImporterCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSSGAssetImporterCall7 call = reinterpret_cast<CuteQSSGAssetImporterCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSSGAssetImporterCall8 call = reinterpret_cast<CuteQSSGAssetImporterCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSSGAssetImporterCall9 call = reinterpret_cast<CuteQSSGAssetImporterCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSSGAssetImporterCall10 call = reinterpret_cast<CuteQSSGAssetImporterCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSSGAssetImporterCall11 call = reinterpret_cast<CuteQSSGAssetImporterCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSSGAssetImporter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QSSGAssetImporter10metaObjectEv(
    const QSSGAssetImporter *self) {
  return self->metaObject();
}

//  QString QSSGAssetImporter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSSGAssetImporter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSSGAssetImporter::tr(s, c, n));
}

//  QString QSSGAssetImporter::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSSGAssetImporter4nameEv(
    const QSSGAssetImporter *self) {
  return new QString(self->name());
}

//  QStringList QSSGAssetImporter::inputExtensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QSSGAssetImporter15inputExtensionsEv(
    const QSSGAssetImporter *self) {
  return new QList<QString>(self->inputExtensions());
}

//  QString QSSGAssetImporter::outputExtension() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSSGAssetImporter15outputExtensionEv(
    const QSSGAssetImporter *self) {
  return new QString(self->outputExtension());
}

//  QString QSSGAssetImporter::type() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSSGAssetImporter4typeEv(
    const QSSGAssetImporter *self) {
  return new QString(self->type());
}

//  QJsonObject QSSGAssetImporter::importOptions() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK17QSSGAssetImporter13importOptionsEv(
    const QSSGAssetImporter *self) {
  return new QJsonObject(self->importOptions());
}

//  QString QSSGAssetImporter::typeDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSSGAssetImporter15typeDescriptionEv(
    const QSSGAssetImporter *self) {
  return new QString(self->typeDescription());
}

//  a Python function taken by a CuteQSSGAssetImporter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSSGAssetImporter(
    QSSGAssetImporter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSSGAssetImporter *>(self)->take(key, call);
}
