//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qabstractprotobufserializer.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtProtobuf/qabstractprotobufserializer.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAbstractProtobufSerializer that Python can take functions over in. Every QAbstractProtobufSerializer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAbstractProtobufSerializerCall0)(const void *, int *);
typedef QString * (*CuteQAbstractProtobufSerializerCall1)(const void *, int *);
typedef const QByteArray * (*CuteQAbstractProtobufSerializerCall2)(const void *, const QProtobufMessage *, int *);
typedef bool (*CuteQAbstractProtobufSerializerCall3)(const void *, QProtobufMessage *, const QByteArrayView *, int *);
class CuteQAbstractProtobufSerializer : public QAbstractProtobufSerializer {
public:
  using QAbstractProtobufSerializer::QAbstractProtobufSerializer;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK27QAbstractProtobufSerializer9lastErrorEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractProtobufSerializer15lastErrorStringEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractProtobufSerializer16serializeMessageEPK16QProtobufMessage")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QAbstractProtobufSerializer18deserializeMessageEP16QProtobufMessage14QByteArrayView")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  Error QAbstractProtobufSerializer::lastError() const
  QAbstractProtobufSerializer::Error lastError() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractProtobufSerializerCall0 call = reinterpret_cast<CuteQAbstractProtobufSerializerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractProtobufSerializer::Error>(given);
    }
    return {};
  }

  //  QString QAbstractProtobufSerializer::lastErrorString() const
  QString lastErrorString() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractProtobufSerializerCall1 call = reinterpret_cast<CuteQAbstractProtobufSerializerCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QByteArray QAbstractProtobufSerializer::serializeMessage(const
  //      QProtobufMessage *message) const
  QByteArray serializeMessage(
      const QProtobufMessage *message) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractProtobufSerializerCall2 call = reinterpret_cast<CuteQAbstractProtobufSerializerCall2>(taken[2]);
      const QByteArray * given = call(this, message, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QAbstractProtobufSerializer::deserializeMessage(QProtobufMessage
  //      *message, QByteArrayView data) const
  bool deserializeMessage(
      QProtobufMessage *message,
      QByteArrayView data) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractProtobufSerializerCall3 call = reinterpret_cast<CuteQAbstractProtobufSerializerCall3>(taken[3]);
      bool given = call(this, message, &data, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QByteArray QAbstractProtobufSerializer::serialize(const QProtobufMessage
//      *message) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK27QAbstractProtobufSerializer9serializeEPK16QProtobufMessage(
    const QAbstractProtobufSerializer *self,
    const QProtobufMessage *message) {
  return new QByteArray(self->serialize(message));
}

//  bool QAbstractProtobufSerializer::deserialize(QProtobufMessage *message,
//      QByteArrayView data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QAbstractProtobufSerializer11deserializeEP16QProtobufMessage14QByteArrayView(
    const QAbstractProtobufSerializer *self,
    QProtobufMessage *message,
    const QByteArrayView *data) {
  return self->deserialize(message, *data);
}

//  QAbstractProtobufSerializer::~QAbstractProtobufSerializer()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractProtobufSerializerD1Ev(
    QAbstractProtobufSerializer *self) {
  delete self;
}

//  Error QAbstractProtobufSerializer::lastError() const
extern "C" Q_DECL_EXPORT
QAbstractProtobufSerializer::Error ritual_ZNK27QAbstractProtobufSerializer9lastErrorEv(
    const QAbstractProtobufSerializer *self) {
  return self->lastError();
}

//  QString QAbstractProtobufSerializer::lastErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QAbstractProtobufSerializer15lastErrorStringEv(
    const QAbstractProtobufSerializer *self) {
  return new QString(self->lastErrorString());
}

//  QByteArray QAbstractProtobufSerializer::serializeMessage(const
//      QProtobufMessage *message) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK27QAbstractProtobufSerializer16serializeMessageEPK16QProtobufMessage(
    const QAbstractProtobufSerializer *self,
    const QProtobufMessage *message) {
  return new QByteArray(self->serializeMessage(message));
}

//  bool QAbstractProtobufSerializer::deserializeMessage(QProtobufMessage
//      *message, QByteArrayView data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QAbstractProtobufSerializer18deserializeMessageEP16QProtobufMessage14QByteArrayView(
    const QAbstractProtobufSerializer *self,
    QProtobufMessage *message,
    const QByteArrayView *data) {
  return self->deserializeMessage(message, *data);
}

//  a Python function taken by a CuteQAbstractProtobufSerializer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractProtobufSerializer(
    QAbstractProtobufSerializer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractProtobufSerializer *>(self)->take(key, call);
}
