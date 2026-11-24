//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qutimimeconverter.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if defined(Q_OS_DARWIN)
#include <QtGui/QtGui>
#include <QtGui/qutimimeconverter.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QUtiMimeConverter that Python can take functions over in. Every QUtiMimeConverter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQUtiMimeConverterCall0)(const void *, const QString *, int *);
typedef QString * (*CuteQUtiMimeConverterCall1)(const void *, const QString *, int *);
typedef int (*CuteQUtiMimeConverterCall2)(const void *, const QMimeData *, int *);
class CuteQUtiMimeConverter : public QUtiMimeConverter {
public:
  using QUtiMimeConverter::QUtiMimeConverter;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QUtiMimeConverter10utiForMimeERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QUtiMimeConverter10mimeForUtiERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QUtiMimeConverter5countEPK9QMimeData")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QString QUtiMimeConverter::utiForMime(const QString &mime) const
  QString utiForMime(const QString &mime) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQUtiMimeConverterCall0 call = reinterpret_cast<CuteQUtiMimeConverterCall0>(taken[0]);
      QString * given = call(this, &mime, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QString QUtiMimeConverter::mimeForUti(const QString &uti) const
  QString mimeForUti(const QString &uti) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQUtiMimeConverterCall1 call = reinterpret_cast<CuteQUtiMimeConverterCall1>(taken[1]);
      QString * given = call(this, &uti, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  int QUtiMimeConverter::count(const QMimeData *mimeData) const
  int count(const QMimeData *mimeData) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQUtiMimeConverterCall2 call = reinterpret_cast<CuteQUtiMimeConverterCall2>(taken[2]);
      int given = call(this, mimeData, &handled);
      if (handled) return given;
    }
    return QUtiMimeConverter::count(mimeData);
  }
};

//  QUtiMimeConverter::~QUtiMimeConverter()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QUtiMimeConverterD1Ev(QUtiMimeConverter *self) {
  delete self;
}

//  HandlerScope QUtiMimeConverter::scope() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QUtiMimeConverter5scopeEv(const QUtiMimeConverter *self) {
  return static_cast<int>(self->scope().toInt());
}

//  bool QUtiMimeConverter::canConvert(const QString &mime, const QString
//      &uti) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QUtiMimeConverter10canConvertERK7QStringS2_(
    const QUtiMimeConverter *self,
    const QString *mime,
    const QString *uti) {
  return self->canConvert(*mime, *uti);
}

//  QList<QByteArray> QUtiMimeConverter::convertFromMime(const QString &mime,
//      const QVariant &data, const QString &uti) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK17QUtiMimeConverter15convertFromMimeERK7QStringRK8QVariantS2_(
    const QUtiMimeConverter *self,
    const QString *mime,
    const QVariant *data,
    const QString *uti) {
  return new QList<QByteArray>(self->convertFromMime(*mime, *data, *uti));
}

//  QString QUtiMimeConverter::utiForMime(const QString &mime) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QUtiMimeConverter10utiForMimeERK7QString(
    const QUtiMimeConverter *self,
    const QString *mime) {
  return new QString(self->utiForMime(*mime));
}

//  QString QUtiMimeConverter::mimeForUti(const QString &uti) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QUtiMimeConverter10mimeForUtiERK7QString(
    const QUtiMimeConverter *self,
    const QString *uti) {
  return new QString(self->mimeForUti(*uti));
}

//  QVariant QUtiMimeConverter::convertToMime(const QString &mime, const
//      QList<QByteArray> &data, const QString &uti) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QUtiMimeConverter13convertToMimeERK7QStringRK5QListI10QByteArrayES2_(
    const QUtiMimeConverter *self,
    const QString *mime,
    const QList<QByteArray> *data,
    const QString *uti) {
  return new QVariant(self->convertToMime(*mime, *data, *uti));
}

//  int QUtiMimeConverter::count(const QMimeData *mimeData) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QUtiMimeConverter5countEPK9QMimeData(
    const QUtiMimeConverter *self,
    const QMimeData *mimeData) {
  return self->count(mimeData);
}

//  a Python function taken by a CuteQUtiMimeConverter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUtiMimeConverter(
    QUtiMimeConverter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQUtiMimeConverter *>(self)->take(key, call);
}

//  int QUtiMimeConverter::count(const QMimeData *mimeData) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QUtiMimeConverter5countEPK9QMimeData(
    const QUtiMimeConverter *self,
    const QMimeData *mimeData) {
  return self->QUtiMimeConverter::count(mimeData);
}

#endif  // defined(Q_OS_DARWIN)
