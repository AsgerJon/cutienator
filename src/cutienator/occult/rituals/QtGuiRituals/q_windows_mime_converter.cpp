//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qwindowsmimeconverter.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: Qt's 'qt_windows.h' is pulled in, as Qt's
//  qwindowsmimeconverter.cpp does, for the COM structs FORMATETC and
//  STGMEDIUM, which Qt's header only names and the rituals that give a
//  QList<FORMATETC> need whole. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#if defined(Q_OS_WIN)
#include <QtGui/QtGui>
#include <QtGui/qwindowsmimeconverter.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qt_windows.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <cstring>
#include <QtCore/QList>
#include <QtCore/QString>

//  A QWindowsMimeConverter that Python can take functions over in. Every QWindowsMimeConverter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQWindowsMimeConverterCall0)(const void *, const QString *, IDataObject *, int *);
typedef const QVariant * (*CuteQWindowsMimeConverterCall1)(const void *, const QString *, IDataObject *, const QMetaType *, int *);
class CuteQWindowsMimeConverter : public QWindowsMimeConverter {
public:
  using QWindowsMimeConverter::QWindowsMimeConverter;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QWindowsMimeConverter16canConvertToMimeERK7QStringP11IDataObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QWindowsMimeConverter13convertToMimeERK7QStringP11IDataObject9QMetaType")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QWindowsMimeConverter::canConvertToMime(const QString &mimeType,
  //      IDataObject *pDataObj) const
  bool canConvertToMime(
      const QString &mimeType,
      IDataObject *pDataObj) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsMimeConverterCall0 call = reinterpret_cast<CuteQWindowsMimeConverterCall0>(taken[0]);
      bool given = call(this, &mimeType, pDataObj, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QVariant QWindowsMimeConverter::convertToMime(const QString
  //      &mimeType, IDataObject *pDataObj, QMetaType preferredType) const
  QVariant convertToMime(
      const QString &mimeType,
      IDataObject *pDataObj,
      QMetaType preferredType) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsMimeConverterCall1 call = reinterpret_cast<CuteQWindowsMimeConverterCall1>(taken[1]);
      const QVariant * given = call(this, &mimeType, pDataObj, &preferredType, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QWindowsMimeConverter::~QWindowsMimeConverter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWindowsMimeConverterD1Ev(QWindowsMimeConverter *self) {
  delete self;
}

//  int QWindowsMimeConverter::registerMimeType(const QString &mimeType)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QWindowsMimeConverter16registerMimeTypeERK7QString(
    const QString *mimeType) {
  return QWindowsMimeConverter::registerMimeType(*mimeType);
}

//  bool QWindowsMimeConverter::canConvertFromMime(const FORMATETC
//      &formatetc, const QMimeData *mimeData) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWindowsMimeConverter18canConvertFromMimeERK12tagFORMATETCPK9QMimeData(
    const QWindowsMimeConverter *self,
    const FORMATETC *formatetc,
    const QMimeData *mimeData) {
  return self->canConvertFromMime(*formatetc, mimeData);
}

//  bool QWindowsMimeConverter::convertFromMime(const FORMATETC &formatetc,
//      const QMimeData *mimeData, STGMEDIUM *pmedium) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWindowsMimeConverter15convertFromMimeERK12tagFORMATETCPK9QMimeDataP12tagSTGMEDIUM(
    const QWindowsMimeConverter *self,
    const FORMATETC *formatetc,
    const QMimeData *mimeData,
    STGMEDIUM *pmedium) {
  return self->convertFromMime(*formatetc, mimeData, pmedium);
}

//  QList<FORMATETC> QWindowsMimeConverter::formatsForMime(const QString
//      &mimeType, const QMimeData *mimeData) const
extern "C" Q_DECL_EXPORT
QList<FORMATETC> *ritual_ZNK21QWindowsMimeConverter14formatsForMimeERK7QStringPK9QMimeData(
    const QWindowsMimeConverter *self,
    const QString *mimeType,
    const QMimeData *mimeData) {
  return new QList<FORMATETC>(self->formatsForMime(*mimeType, mimeData));
}

//  bool QWindowsMimeConverter::canConvertToMime(const QString &mimeType,
//      IDataObject *pDataObj) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWindowsMimeConverter16canConvertToMimeERK7QStringP11IDataObject(
    const QWindowsMimeConverter *self,
    const QString *mimeType,
    IDataObject *pDataObj) {
  return self->canConvertToMime(*mimeType, pDataObj);
}

//  QVariant QWindowsMimeConverter::convertToMime(const QString &mimeType,
//      IDataObject *pDataObj, QMetaType preferredType) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QWindowsMimeConverter13convertToMimeERK7QStringP11IDataObject9QMetaType(
    const QWindowsMimeConverter *self,
    const QString *mimeType,
    IDataObject *pDataObj,
    const QMetaType *preferredType) {
  return new QVariant(
      self->convertToMime(
          *mimeType,
          pDataObj,
          *preferredType));
}

//  QString QWindowsMimeConverter::mimeForFormat(const FORMATETC &formatetc)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWindowsMimeConverter13mimeForFormatERK12tagFORMATETC(
    const QWindowsMimeConverter *self,
    const FORMATETC *formatetc) {
  return new QString(self->mimeForFormat(*formatetc));
}

//  a Python function taken by a CuteQWindowsMimeConverter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsMimeConverter(
    QWindowsMimeConverter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsMimeConverter *>(self)->take(key, call);
}

//  a QList<FORMATETC> a ritual of QWindowsMimeConverter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWindowsMimeConverter__QList_FORMATETC(
    QList<FORMATETC> *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
