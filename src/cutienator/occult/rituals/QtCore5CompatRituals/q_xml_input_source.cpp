//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qchar.h>
#include <cstring>

//  Only a class built on QXmlInputSource may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQXmlInputSource : QXmlInputSource {
  using QXmlInputSource::fromRawData;
};

//  A QXmlInputSource that Python can take functions over in. Every QXmlInputSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQXmlInputSourceCall0)(const void *, const QString *, int *);
typedef void (*CuteQXmlInputSourceCall1)(const void *, const QByteArray *, int *);
typedef void (*CuteQXmlInputSourceCall2)(const void *, int *);
typedef QString * (*CuteQXmlInputSourceCall3)(const void *, int *);
typedef const QChar * (*CuteQXmlInputSourceCall4)(const void *, int *);
typedef void (*CuteQXmlInputSourceCall5)(const void *, int *);
typedef QString * (*CuteQXmlInputSourceCall6)(const void *, const QByteArray *, bool, int *);
class CuteQXmlInputSource : public QXmlInputSource {
public:
  using QXmlInputSource::QXmlInputSource;
  CuteQXmlInputSource(const QXmlInputSource &other) : QXmlInputSource(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QXmlInputSource7setDataERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlInputSource7setDataERK10QByteArray")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlInputSource9fetchDataEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QXmlInputSource4dataEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlInputSource4nextEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlInputSource5resetEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QXmlInputSource11fromRawDataERK10QByteArrayb")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QXmlInputSource::setData(const QString &dat)
  void setData(const QString &dat) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlInputSourceCall0 call = reinterpret_cast<CuteQXmlInputSourceCall0>(taken[0]);
      call(this, &dat, &handled);
      if (handled) return;
    }
    QXmlInputSource::setData(dat);
  }

  //  void QXmlInputSource::setData(const QByteArray &dat)
  void setData(const QByteArray &dat) override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlInputSourceCall1 call = reinterpret_cast<CuteQXmlInputSourceCall1>(taken[1]);
      call(this, &dat, &handled);
      if (handled) return;
    }
    QXmlInputSource::setData(dat);
  }

  //  void QXmlInputSource::fetchData()
  void fetchData() override {
    if (taken[2]) {
      int handled = 0;
      CuteQXmlInputSourceCall2 call = reinterpret_cast<CuteQXmlInputSourceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QXmlInputSource::fetchData();
  }

  //  QString QXmlInputSource::data() const
  QString data() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQXmlInputSourceCall3 call = reinterpret_cast<CuteQXmlInputSourceCall3>(taken[3]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QXmlInputSource::data();
  }

  //  QChar QXmlInputSource::next()
  QChar next() override {
    if (taken[4]) {
      int handled = 0;
      CuteQXmlInputSourceCall4 call = reinterpret_cast<CuteQXmlInputSourceCall4>(taken[4]);
      const QChar * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QXmlInputSource::next();
  }

  //  void QXmlInputSource::reset()
  void reset() override {
    if (taken[5]) {
      int handled = 0;
      CuteQXmlInputSourceCall5 call = reinterpret_cast<CuteQXmlInputSourceCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QXmlInputSource::reset();
  }

  //  QString QXmlInputSource::fromRawData(const QByteArray &data, bool
  //      beginning)
  QString fromRawData(const QByteArray &data, bool beginning) override {
    if (taken[6]) {
      int handled = 0;
      CuteQXmlInputSourceCall6 call = reinterpret_cast<CuteQXmlInputSourceCall6>(taken[6]);
      QString * given = call(this, &data, beginning, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QXmlInputSource::fromRawData(data, beginning);
  }
};

//  QXmlInputSource::QXmlInputSource()
extern "C" Q_DECL_EXPORT
QXmlInputSource *ritual_ZN15QXmlInputSourceC1Ev() {
  return new CuteQXmlInputSource();
}

//  QXmlInputSource::QXmlInputSource(QIODevice *dev)
extern "C" Q_DECL_EXPORT
QXmlInputSource *ritual_ZN15QXmlInputSourceC1EP9QIODevice(QIODevice *dev) {
  return new CuteQXmlInputSource(dev);
}

//  QXmlInputSource::~QXmlInputSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QXmlInputSourceD1Ev(QXmlInputSource *self) {
  delete self;
}

//  void QXmlInputSource::setData(const QString &dat)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QXmlInputSource7setDataERK7QString(
    QXmlInputSource *self,
    const QString *dat) {
  self->setData(*dat);
}

//  void QXmlInputSource::setData(const QByteArray &dat)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QXmlInputSource7setDataERK10QByteArray(
    QXmlInputSource *self,
    const QByteArray *dat) {
  self->setData(*dat);
}

//  void QXmlInputSource::fetchData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QXmlInputSource9fetchDataEv(QXmlInputSource *self) {
  self->fetchData();
}

//  QString QXmlInputSource::data() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QXmlInputSource4dataEv(const QXmlInputSource *self) {
  return new QString(self->data());
}

//  QChar QXmlInputSource::next()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN15QXmlInputSource4nextEv(QXmlInputSource *self) {
  return new QChar(self->next());
}

//  void QXmlInputSource::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QXmlInputSource5resetEv(QXmlInputSource *self) {
  self->reset();
}

//  QString QXmlInputSource::fromRawData(const QByteArray &data, bool
//      beginning)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QXmlInputSource11fromRawDataERK10QByteArrayb(
    QXmlInputSource *self,
    const QByteArray *data,
    bool beginning) {
  return new QString(self->fromRawData(*data, beginning));
}

//  void QXmlInputSource::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QXmlInputSource4initEv(QXmlInputSource *self) {
  self->init();
}

//  a Python function taken by a CuteQXmlInputSource, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlInputSource(
    QXmlInputSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlInputSource *>(self)->take(key, call);
}

//  void QXmlInputSource::setData(const QString &dat)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QXmlInputSource7setDataERK7QString(
    QXmlInputSource *self,
    const QString *dat) {
  self->QXmlInputSource::setData(*dat);
}

//  void QXmlInputSource::setData(const QByteArray &dat)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QXmlInputSource7setDataERK10QByteArray(
    QXmlInputSource *self,
    const QByteArray *dat) {
  self->QXmlInputSource::setData(*dat);
}

//  void QXmlInputSource::fetchData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QXmlInputSource9fetchDataEv(QXmlInputSource *self) {
  self->QXmlInputSource::fetchData();
}

//  QString QXmlInputSource::data() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QXmlInputSource4dataEv(
    const QXmlInputSource *self) {
  return new QString(self->QXmlInputSource::data());
}

//  QChar QXmlInputSource::next()
extern "C" Q_DECL_EXPORT
QChar *ritual_own_ZN15QXmlInputSource4nextEv(QXmlInputSource *self) {
  return new QChar(self->QXmlInputSource::next());
}

//  void QXmlInputSource::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QXmlInputSource5resetEv(QXmlInputSource *self) {
  self->QXmlInputSource::reset();
}

//  QString QXmlInputSource::fromRawData(const QByteArray &data, bool
//      beginning)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN15QXmlInputSource11fromRawDataERK10QByteArrayb(
    QXmlInputSource *self,
    const QByteArray *data,
    bool beginning) {
  return new QString(
      static_cast<OwnQXmlInputSource *>(self)->OwnQXmlInputSource::fromRawData(
          *data,
          beginning));
}
