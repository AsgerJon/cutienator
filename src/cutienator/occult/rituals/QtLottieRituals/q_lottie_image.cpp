//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieimage_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QLottieImage that Python can take functions over in. Every QLottieImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieImageCall0)(const void *, int *);
typedef bool (*CuteQLottieImageCall1)(const void *, int, const QVariant *, int *);
typedef int (*CuteQLottieImageCall2)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieImageCall3)(const void *, int, int *);
typedef void * (*CuteQLottieImageCall4)(const void *, const QString *, int *);
typedef void (*CuteQLottieImageCall5)(const void *, int, int *);
typedef const QSize * (*CuteQLottieImageCall6)(const void *, int *);
class CuteQLottieImage : public QLottieImage {
public:
  using QLottieImage::QLottieImage;
  CuteQLottieImage(const QLottieImage &other) : QLottieImage(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieImage::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieImageCall0 call = reinterpret_cast<CuteQLottieImageCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieImage::clone();
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieImageCall1 call = reinterpret_cast<CuteQLottieImageCall1>(taken[1]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  int QLottieBase::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieImageCall2 call = reinterpret_cast<CuteQLottieImageCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieBase::parse(definition);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieImageCall3 call = reinterpret_cast<CuteQLottieImageCall3>(taken[3]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieImageCall4 call = reinterpret_cast<CuteQLottieImageCall4>(taken[4]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  void QLottieBase::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieImageCall5 call = reinterpret_cast<CuteQLottieImageCall5>(taken[5]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieBase::updateProperties(frame);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieImageCall6 call = reinterpret_cast<CuteQLottieImageCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieImage::QLottieImage(const QLottieImage &other)
extern "C" Q_DECL_EXPORT
QLottieImage *ritual_ZN12QLottieImageC1ERKS_(const QLottieImage *other) {
  return new CuteQLottieImage(*other);
}

//  QLottieImage::QLottieImage(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieImage *ritual_ZN12QLottieImageC1EP11QLottieBase(QLottieBase *parent) {
  return new CuteQLottieImage(parent);
}

//  QLottieBase *QLottieImage::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK12QLottieImage5cloneEv(const QLottieImage *self) {
  return self->clone();
}

//  int QLottieImage::construct(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QLottieImage9constructERK11QJsonObject(
    QLottieImage *self,
    const QJsonObject *definition) {
  return self->construct(*definition);
}

//  QUrl QLottieImage::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QLottieImage3urlEv(const QLottieImage *self) {
  return new QUrl(self->url());
}

//  QSizeF QLottieImage::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK12QLottieImage4sizeEv(const QLottieImage *self) {
  return new QSizeF(self->size());
}

//  QImage QLottieImage::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK12QLottieImage5imageEv(const QLottieImage *self) {
  return new QImage(self->image());
}

//  QLottieImage::~QLottieImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieImageD1Ev(QLottieImage *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieImage, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieImage(
    QLottieImage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieImage *>(self)->take(key, call);
}

//  QLottieBase *QLottieImage::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK12QLottieImage5cloneEv(const QLottieImage *self) {
  return self->QLottieImage::clone();
}
